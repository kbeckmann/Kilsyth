`default_nettype none

module kilsyth_top(
	input wire i_clk16,

	/* ft600 interface */
	inout  wire [15:0] io_ft_data,
	input  wire        i_ft_clk,
	output wire [ 1:0] i_ft_be,
	output wire        i_ft_txe_n,
	output wire        i_ft_rxf_n,
	input  wire        i_ft_wr_n,
	input  wire        i_ft_rd_n,
	input  wire        i_ft_oe_n,
	inout  wire        io_ft_gpio1,

	/* SDRAM */
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

	/* PMODs */
	inout  wire [ 7:0] io_pmod_0,
	inout  wire [ 7:0] io_pmod_1,
	inout  wire [ 7:0] io_pmod_2,

	/* 40-pin wide header */
	inout  wire [39:0] io_wide
);

	reg [25:0] counter = 0;
	assign io_wide[39:32] = (counter[0] == 0) ? counter[25:18] : 'bz; /* Show counter on LEDs */
	/* Trigger BiDir on the inout pins */
	assign io_wide[31: 0] = (counter[0] == 0) ? 'b0 : 'bz;
	assign io_ft_data = (counter[0] == 0) ? 'b0 : 'bz;
	assign io_sdram_dq = (counter[0] == 0) ? 'b0 : 'bz;
	//assign io_pmod_0 = (counter[0] == 0) ? 'b0 : 'bz;
	assign io_pmod_1 = (counter[0] == 0) ? 'b0 : 'bz;
	assign io_pmod_2 = (counter[0] == 0) ? 'b0 : 'bz;

	/* Read everything that is readable */
	assign io_pmod_0 = &{
		io_ft_data,
		i_ft_clk,
		i_ft_wr_n,
		i_ft_rd_n,
		i_ft_oe_n,
		io_ft_gpio1,
		io_sdram_dq,
		io_pmod_1,
		io_pmod_2,
		io_wide
		} ? 'b1 : 'bz;

	always @(posedge i_clk16) begin
		if (io_ft_gpio1) begin
			/* act as reset */
			counter <= 0;
		end else begin
			counter <= counter + 1;
		end
	end


endmodule
