`default_nettype none

module kilsyth_top(
	input wire i_clk16,

	output wire[7:0] o_leds
);

	reg [25:0] counter = 0;
	reg [7:0] leds = 0;
	assign o_leds = leds;
	
	/* This clock is _always_ ticking */
	always @(posedge i_clk16) begin
		counter    <= counter + 1;
		leds       <= counter[25:25-7];
	end

endmodule
