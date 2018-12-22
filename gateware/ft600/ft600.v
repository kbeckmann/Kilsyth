`default_nettype none

module kilsyth_top(
	input wire i_clk16,

	/* ft600 interface */
	inout  wire [15:0] io_ft_data,
	input  wire        i_ft_clk,
	inout  wire [ 1:0] io_ft_be,
	input  wire        i_ft_txe_n,
	input  wire        i_ft_rxf_n,
	output wire        o_ft_wr_n,
	output wire        o_ft_rd_n,
	inout  wire        io_ft_oe_n,
	inout  wire        io_ft_gpio1,

	/* SDRAM */
/*
	inout  wire [15:0] io_sdram_dq,
	output wire [ 1:0] o_sdram_dqm,
	output wire [12:0] o_sdram_a,
	output wire [ 1:0] o_sdram_ba,
	output wire        o_sdram_cs_n,
	output wire        o_sdram_ras_n,
	output wire        o_sdram_cas_n,
	output wire        o_sdram_we_n,
	output wire        o_sdram_clk_n,
	output wire        o_sdram_cke_n,
*/
	/* PMODs */
/*
	inout  wire [ 7:0] io_pmod_0,
	inout  wire [ 7:0] io_pmod_1,
	inout  wire [ 7:0] io_pmod_2,
*/
	/* 40-pin wide header */
/*
	inout  wire [39:0] io_wide
*/
	output wire[7:0] o_leds
);

	reg [25:0] counter = 0;
	reg [7:0] leds = 0;
	assign o_leds = leds;
	
	/* Read datasheet and figure out this stuff */
	reg ft_oe_n = 1;
	assign io_ft_oe_n = ft_oe_n;
	reg ft_wr_n = 1;
	assign o_ft_wr_n = ft_wr_n;
	reg ft_rd_n = 1;
	assign o_ft_rd_n = ft_rd_n;

	reg [15:0] ft_data_buf = 'b0;
	reg ft_data_dir = 0;
	assign io_ft_data = ft_data_dir ? ft_data_buf : 'bz;

	// Getting weird tristate bug???
	// reg [1:0] ft_be = 2'b00;
	// assign io_ft_be = ft_data_dir ? ft_be : 2'bzz;

	/* This clock is _always_ ticking */
	always @(posedge i_clk16) begin
		counter    <= counter + 1;
		leds[0]    <= counter[23];
		leds[2:1]  <= io_ft_be;
		leds[3]    <= i_ft_txe_n;
		leds[4]    <= i_ft_rxf_n;
		leds[5]    <= ft_rd_n; 
	end

	reg [7:0] state = 0;
	reg [7:0] next_state = 0;
	
	reg [31:0] tx_words;
	reg wants_to_write = 0;
	
	reg [15:0] fifo_buf[0:1023];
	reg [31:0] index;
	reg [15:0] ft_counter = 0;
	
	/* This clock might only tick while there is a transfer ongoing, not sure... */
	always @(posedge i_ft_clk) begin
		leds[6]    <= ~leds[6];
		leds[7]    <= wants_to_write;
		
		state      <= next_state;
		case (state)
			0: begin
				ft_oe_n <= 1;
				ft_rd_n <= 1;
				ft_wr_n <= 1;
				ft_data_dir <= 0;
				
				if (!i_ft_txe_n && wants_to_write) begin
					wants_to_write <= 0;
					next_state <= 3;
				end else if (!i_ft_rxf_n) begin
					ft_oe_n <= 0;
					ft_rd_n <= 0;
					//words_to_read <= 1024;
					index <= 0;
					next_state <= 1;
				end
			end
			1: begin
				// read a word..
				//ft_data_buf <= io_ft_data;
				//fifo_buf[index] <= io_ft_data;
				//index <= index + 1;
				//if (i_ft_rxf_n || index == 0) begin
				if (i_ft_rxf_n) begin
					wants_to_write <= 1;
					next_state <= 0;
				end
			end
			3: begin
				ft_oe_n <= 1;
				ft_wr_n <= 0;
				// ft_be <= 2'b11;
				ft_data_buf <= 16'h42;
				tx_words <= 16;
				ft_data_dir <= 1;
				next_state <= 4;
			end
			4: begin
				ft_data_buf <= 16'hFF;
//				ft_data_buf <= ft_counter;
//				ft_counter <= ft_counter + 1;
//				if (!i_ft_txe_n)
	//				tx_words <= tx_words - 1;

		//		if (tx_words == 0) begin
			//	if (i_ft_txe_n) begin
					next_state <= 0;
					wants_to_write <= 0;
				//end
			end
		endcase
	end


endmodule
