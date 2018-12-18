`default_nettype none

module kilsyth_top(
	input wire i_clk16,

	/* ft600 interface */
	inout  wire [15:0] io_ft_data,
	input  wire        i_ft_clk,
	input  wire [ 1:0] i_ft_be,
	output wire        o_ft_txe_n,
	output wire        o_ft_rxf_n,
	input  wire        i_ft_wr_n,
	input  wire        i_ft_rd_n,
	input  wire        i_ft_oe_n,
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
	reg ft_txe_n = 1;
	assign o_ft_txe_n = ft_txe_n;
	reg ft_rxf_n = 1;
	assign o_ft_rxf_n = ft_rxf_n;

	/* This clock is _always_ ticking */
	always @(posedge i_clk16) begin
		counter    <= counter + 1;
		leds[0]    <= counter[23];
		leds[2:1]  <= i_ft_be;
		leds[3]    <= i_ft_wr_n;
		leds[4]    <= i_ft_rd_n;
		leds[5]    <= i_ft_oe_n;
		leds[6]    <= io_ft_gpio1;
	end

	/* This clock might only tick while there is a transfer ongoing, not sure... */
	always @(posedge i_ft_clk) begin
		leds[7] <= |io_ft_data;
	end


endmodule
