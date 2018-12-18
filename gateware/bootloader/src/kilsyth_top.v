`default_nettype none

module kilsyth_top(
	input wire i_clk16,

	/* ft600 interface */
/*
	inout  wire [15:0] io_ft_data,
	input  wire        i_ft_clk,
	output wire [ 1:0] i_ft_be,
	output wire        i_ft_txe_n,
	output wire        i_ft_rxf_n,
	input  wire        i_ft_wr_n,
	input  wire        i_ft_rd_n,
	input  wire        i_ft_oe_n,
	inout  wire        io_ft_gpio1,
/*
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
/*
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
	assign o_leds = counter[25:25-7];

	always @(posedge i_clk16) begin
		counter <= counter + 1;
	end


endmodule
