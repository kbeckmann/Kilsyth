// Verilog netlist produced by program LSE :  version Diamond (64-bit) 3.10.3.144.3
// Netlist written on Tue Dec 11 23:35:38 2018
//
// Verilog Description of module kilsyth_top
//

module kilsyth_top (i_clk16, io_ft_data, i_ft_clk, i_ft_be, i_ft_txe_n, 
            i_ft_rxf_n, i_ft_wr_n, i_ft_rd_n, i_ft_oe_n, io_ft_gpio1, 
            io_sdram_dq, o_sdram_dqm, o_sdram_a, o_sdram_ba, o_sdram_cs_n, 
            o_sdram_ras_n, o_sdram_cas_n, o_sdram_we_n, o_sdram_clk_n, 
            o_sdram_cke_n, io_pmod_0, io_pmod_1, io_pmod_2, io_wide) /* synthesis syn_module_defined=1 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(3[8:19])
    input i_clk16;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(4[13:20])
    inout [15:0]io_ft_data;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(7[21:31])
    input i_ft_clk;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(8[21:29])
    output [1:0]i_ft_be;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(9[21:28])
    output i_ft_txe_n;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(10[21:31])
    output i_ft_rxf_n;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(11[21:31])
    input i_ft_wr_n;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(12[21:30])
    input i_ft_rd_n;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(13[21:30])
    input i_ft_oe_n;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(14[21:30])
    input io_ft_gpio1 /* synthesis .original_dir=IN_OUT */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(15[21:32])
    inout [15:0]io_sdram_dq;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(18[21:32])
    output [1:0]o_sdram_dqm;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(19[21:32])
    output [12:0]o_sdram_a;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(20[21:30])
    output [1:0]o_sdram_ba;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(21[21:31])
    output o_sdram_cs_n;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(22[21:33])
    output o_sdram_ras_n;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(23[21:34])
    output o_sdram_cas_n;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(24[21:34])
    output o_sdram_we_n;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(25[21:33])
    output o_sdram_clk_n;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(26[21:34])
    output o_sdram_cke_n;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(27[21:34])
    output [7:0]io_pmod_0;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(30[21:30])
    inout [7:0]io_pmod_1;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(31[21:30])
    inout [7:0]io_pmod_2;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(32[21:30])
    inout [39:0]io_wide;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(35[21:28])
    
    wire GND_net /* synthesis RESET_NET_FOR_BUS20=20, DSPPORT_20=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(9[21:28])
    wire VCC_net /* synthesis CE_NET_FOR_BUS20=20, DSPPORT_20=CE3 */ ;
    wire i_clk16_c /* synthesis DSPPORT_20=CLK3, CLOCK_NET_FOR_BUS20=20, is_clock=1, SET_AS_NETWORK=i_clk16_c */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(4[13:20])
    
    wire i_ft_clk_c, n25, n24, n23, n22, i_ft_wr_n_c, i_ft_rd_n_c, 
        i_ft_oe_n_c, io_ft_gpio1_c, n21, n184, n182, n180, n178, 
        n175, n174, n172, n171, n170;
    wire [25:0]counter;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(38[13:20])
    
    wire n168, n166, n165, n164, n162, n160, n158, n156, n154, 
        io_pmod_0_7__N_2, n152, n150, n148, n147, n146, n144, 
        n142, n140, n136, n132, n131, n128, n124, n120, n116, 
        n115, n112, n104, n20, n19, n18, n17, n16, n15, n14, 
        n13, n12, n11, n10, n9, io_ft_data_out_15, n110, n111, 
        n112_adj_1, n113, n114, n115_adj_2, n116_adj_3, n117, n118, 
        n119, n120_adj_4, n121, n122, n123, n124_adj_5, n125, 
        n126, n127, n128_adj_6, n129, n130, n131_adj_7, n132_adj_8, 
        n133, n134, n135, n953, n952, n949, n948, n947, n946, 
        n951, n950, n945, n954, n944, n943, n942, io_ft_data_out_14, 
        io_ft_data_out_13, io_ft_data_out_12, io_ft_data_out_11, io_ft_data_out_10, 
        io_ft_data_out_9, io_ft_data_out_8, io_ft_data_out_7, io_ft_data_out_6, 
        io_ft_data_out_5, io_ft_data_out_4, io_ft_data_out_3, io_ft_data_out_2, 
        io_ft_data_out_1, io_ft_data_out_0, io_sdram_dq_out_15, io_sdram_dq_out_14, 
        io_sdram_dq_out_13, io_sdram_dq_out_12, io_sdram_dq_out_11, io_sdram_dq_out_10, 
        io_sdram_dq_out_9, io_sdram_dq_out_8, io_sdram_dq_out_7, io_sdram_dq_out_6, 
        io_sdram_dq_out_5, io_sdram_dq_out_4, io_sdram_dq_out_3, io_sdram_dq_out_2, 
        io_sdram_dq_out_1, io_sdram_dq_out_0, io_pmod_1_out_7, io_pmod_1_out_6, 
        io_pmod_1_out_5, io_pmod_1_out_4, io_pmod_1_out_3, io_pmod_1_out_2, 
        io_pmod_1_out_1, io_pmod_1_out_0, io_pmod_2_out_7, io_pmod_2_out_6, 
        io_pmod_2_out_5, io_pmod_2_out_4, io_pmod_2_out_3, io_pmod_2_out_2, 
        io_pmod_2_out_1, io_pmod_2_out_0, io_wide_out_39, io_wide_out_38, 
        io_wide_out_37, io_wide_out_36, io_wide_out_35, io_wide_out_34, 
        io_wide_out_33, io_wide_out_32, io_wide_out_31, io_wide_out_30, 
        io_wide_out_29, io_wide_out_28, io_wide_out_27, io_wide_out_26, 
        io_wide_out_25, io_wide_out_24, io_wide_out_23, io_wide_out_22, 
        io_wide_out_21, io_wide_out_20, io_wide_out_19, io_wide_out_18, 
        io_wide_out_17, io_wide_out_16, io_wide_out_15, io_wide_out_14, 
        io_wide_out_13, io_wide_out_12, io_wide_out_11, io_wide_out_10, 
        io_wide_out_9, io_wide_out_8, io_wide_out_7, io_wide_out_6, 
        io_wide_out_5, io_wide_out_4, io_wide_out_3, io_wide_out_2, 
        io_wide_out_1, io_wide_out_0, n100, n96;
    
    VHI i2 (.Z(VCC_net));
    BB io_ft_data_pad_15 (.I(GND_net), .T(counter[0]), .B(io_ft_data[15]), 
       .O(io_ft_data_out_15));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(42[9:19])
    FD1S3IX counter_327__i0 (.D(n135), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(counter[0])) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i0.GSR = "ENABLED";
    LUT4 i35_2_lut (.A(io_wide_out_26), .B(io_wide_out_7), .Z(n128)) /* synthesis lut_function=(A (B)) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i35_2_lut.init = 16'h8888;
    FD1S3IX counter_327__i25 (.D(n110), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(counter[25])) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i25.GSR = "ENABLED";
    LUT4 i77_4_lut (.A(io_sdram_dq_out_3), .B(n154), .C(n120), .D(io_sdram_dq_out_13), 
         .Z(n170)) /* synthesis lut_function=(A (B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i77_4_lut.init = 16'h8000;
    LUT4 i51_4_lut (.A(io_wide_out_20), .B(io_pmod_2_out_7), .C(io_ft_data_out_8), 
         .D(io_pmod_1_out_1), .Z(n144)) /* synthesis lut_function=(A (B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i51_4_lut.init = 16'h8000;
    LUT4 i7_2_lut (.A(io_pmod_1_out_5), .B(io_ft_data_out_9), .Z(n100)) /* synthesis lut_function=(A (B)) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i7_2_lut.init = 16'h8888;
    LUT4 i53_4_lut (.A(io_pmod_2_out_4), .B(i_ft_wr_n_c), .C(io_wide_out_38), 
         .D(io_sdram_dq_out_5), .Z(n146)) /* synthesis lut_function=(A (B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i53_4_lut.init = 16'h8000;
    LUT4 i11_2_lut (.A(io_wide_out_34), .B(io_wide_out_36), .Z(n104)) /* synthesis lut_function=(A (B)) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i11_2_lut.init = 16'h8888;
    BB io_ft_data_pad_14 (.I(GND_net), .T(counter[0]), .B(io_ft_data[14]), 
       .O(io_ft_data_out_14));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(42[9:19])
    BB io_ft_data_pad_13 (.I(GND_net), .T(counter[0]), .B(io_ft_data[13]), 
       .O(io_ft_data_out_13));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(42[9:19])
    BB io_ft_data_pad_12 (.I(GND_net), .T(counter[0]), .B(io_ft_data[12]), 
       .O(io_ft_data_out_12));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(42[9:19])
    BB io_ft_data_pad_11 (.I(GND_net), .T(counter[0]), .B(io_ft_data[11]), 
       .O(io_ft_data_out_11));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(42[9:19])
    BB io_ft_data_pad_10 (.I(GND_net), .T(counter[0]), .B(io_ft_data[10]), 
       .O(io_ft_data_out_10));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(42[9:19])
    BB io_ft_data_pad_9 (.I(GND_net), .T(counter[0]), .B(io_ft_data[9]), 
       .O(io_ft_data_out_9));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(42[9:19])
    BB io_ft_data_pad_8 (.I(GND_net), .T(counter[0]), .B(io_ft_data[8]), 
       .O(io_ft_data_out_8));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(42[9:19])
    BB io_ft_data_pad_7 (.I(GND_net), .T(counter[0]), .B(io_ft_data[7]), 
       .O(io_ft_data_out_7));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(42[9:19])
    LUT4 i568_4_lut (.A(n171), .B(n184), .C(n180), .D(n172), .Z(io_pmod_0_7__N_2)) /* synthesis lut_function=(!(A (B (C (D))))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[9:18])
    defparam i568_4_lut.init = 16'h7fff;
    BB io_ft_data_pad_6 (.I(GND_net), .T(counter[0]), .B(io_ft_data[6]), 
       .O(io_ft_data_out_6));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(42[9:19])
    BB io_ft_data_pad_5 (.I(GND_net), .T(counter[0]), .B(io_ft_data[5]), 
       .O(io_ft_data_out_5));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(42[9:19])
    PUR PUR_INST (.PUR(VCC_net));
    defparam PUR_INST.RST_PULSE = 1;
    BB io_ft_data_pad_4 (.I(GND_net), .T(counter[0]), .B(io_ft_data[4]), 
       .O(io_ft_data_out_4));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(42[9:19])
    LUT4 i78_4_lut (.A(io_sdram_dq_out_8), .B(n156), .C(n124), .D(io_sdram_dq_out_0), 
         .Z(n171)) /* synthesis lut_function=(A (B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i78_4_lut.init = 16'h8000;
    BB io_ft_data_pad_3 (.I(GND_net), .T(counter[0]), .B(io_ft_data[3]), 
       .O(io_ft_data_out_3));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(42[9:19])
    LUT4 i91_4_lut (.A(n175), .B(n182), .C(n165), .D(n166), .Z(n184)) /* synthesis lut_function=(A (B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i91_4_lut.init = 16'h8000;
    BB io_ft_data_pad_2 (.I(GND_net), .T(counter[0]), .B(io_ft_data[2]), 
       .O(io_ft_data_out_2));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(42[9:19])
    BB io_ft_data_pad_1 (.I(GND_net), .T(counter[0]), .B(io_ft_data[1]), 
       .O(io_ft_data_out_1));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(42[9:19])
    LUT4 i22_2_lut (.A(io_wide_out_21), .B(io_ft_data_out_0), .Z(n115)) /* synthesis lut_function=(A (B)) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i22_2_lut.init = 16'h8888;
    BB io_ft_data_pad_0 (.I(GND_net), .T(counter[0]), .B(io_ft_data[0]), 
       .O(io_ft_data_out_0));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(42[9:19])
    LUT4 i87_4_lut (.A(n131), .B(n174), .C(n160), .D(n132), .Z(n180)) /* synthesis lut_function=(A (B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i87_4_lut.init = 16'h8000;
    BB io_sdram_dq_pad_15 (.I(GND_net), .T(counter[0]), .B(io_sdram_dq[15]), 
       .O(io_sdram_dq_out_15));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(43[9:20])
    LUT4 i79_4_lut (.A(io_pmod_1_out_4), .B(n158), .C(n128), .D(io_wide_out_35), 
         .Z(n172)) /* synthesis lut_function=(A (B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i79_4_lut.init = 16'h8000;
    BB io_sdram_dq_pad_14 (.I(GND_net), .T(counter[0]), .B(io_sdram_dq[14]), 
       .O(io_sdram_dq_out_14));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(43[9:20])
    BB io_sdram_dq_pad_13 (.I(GND_net), .T(counter[0]), .B(io_sdram_dq[13]), 
       .O(io_sdram_dq_out_13));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(43[9:20])
    BB io_sdram_dq_pad_12 (.I(GND_net), .T(counter[0]), .B(io_sdram_dq[12]), 
       .O(io_sdram_dq_out_12));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(43[9:20])
    LUT4 i63_4_lut (.A(io_wide_out_1), .B(io_wide_out_14), .C(io_wide_out_28), 
         .D(io_wide_out_6), .Z(n156)) /* synthesis lut_function=(A (B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i63_4_lut.init = 16'h8000;
    BB io_sdram_dq_pad_11 (.I(GND_net), .T(counter[0]), .B(io_sdram_dq[11]), 
       .O(io_sdram_dq_out_11));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(43[9:20])
    LUT4 i31_2_lut (.A(io_ft_data_out_14), .B(io_wide_out_11), .Z(n124)) /* synthesis lut_function=(A (B)) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i31_2_lut.init = 16'h8888;
    BB io_sdram_dq_pad_10 (.I(GND_net), .T(counter[0]), .B(io_sdram_dq[10]), 
       .O(io_sdram_dq_out_10));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(43[9:20])
    BB io_sdram_dq_pad_9 (.I(GND_net), .T(counter[0]), .B(io_sdram_dq[9]), 
       .O(io_sdram_dq_out_9));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(43[9:20])
    LUT4 i23_2_lut (.A(io_pmod_2_out_5), .B(io_pmod_1_out_2), .Z(n116)) /* synthesis lut_function=(A (B)) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i23_2_lut.init = 16'h8888;
    BB io_sdram_dq_pad_8 (.I(GND_net), .T(counter[0]), .B(io_sdram_dq[8]), 
       .O(io_sdram_dq_out_8));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(43[9:20])
    LUT4 i82_4_lut (.A(io_pmod_2_out_3), .B(n164), .C(n140), .D(io_wide_out_27), 
         .Z(n175)) /* synthesis lut_function=(A (B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i82_4_lut.init = 16'h8000;
    BB io_sdram_dq_pad_7 (.I(GND_net), .T(counter[0]), .B(io_sdram_dq[7]), 
       .O(io_sdram_dq_out_7));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(43[9:20])
    LUT4 i89_4_lut (.A(n147), .B(n178), .C(n168), .D(n148), .Z(n182)) /* synthesis lut_function=(A (B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i89_4_lut.init = 16'h8000;
    BB io_sdram_dq_pad_6 (.I(GND_net), .T(counter[0]), .B(io_sdram_dq[6]), 
       .O(io_sdram_dq_out_6));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(43[9:20])
    BB io_sdram_dq_pad_5 (.I(GND_net), .T(counter[0]), .B(io_sdram_dq[5]), 
       .O(io_sdram_dq_out_5));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(43[9:20])
    VLO i1 (.Z(GND_net));
    BB io_sdram_dq_pad_4 (.I(GND_net), .T(counter[0]), .B(io_sdram_dq[4]), 
       .O(io_sdram_dq_out_4));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(43[9:20])
    LUT4 i72_4_lut (.A(io_wide_out_23), .B(n144), .C(n100), .D(io_wide_out_10), 
         .Z(n165)) /* synthesis lut_function=(A (B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i72_4_lut.init = 16'h8000;
    BB io_sdram_dq_pad_3 (.I(GND_net), .T(counter[0]), .B(io_sdram_dq[3]), 
       .O(io_sdram_dq_out_3));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(43[9:20])
    LUT4 i73_4_lut (.A(io_wide_out_30), .B(n146), .C(n104), .D(io_wide_out_39), 
         .Z(n166)) /* synthesis lut_function=(A (B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i73_4_lut.init = 16'h8000;
    BB io_sdram_dq_pad_2 (.I(GND_net), .T(counter[0]), .B(io_sdram_dq[2]), 
       .O(io_sdram_dq_out_2));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(43[9:20])
    BB io_sdram_dq_pad_1 (.I(GND_net), .T(counter[0]), .B(io_sdram_dq[1]), 
       .O(io_sdram_dq_out_1));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(43[9:20])
    LUT4 i59_4_lut (.A(io_ft_data_out_6), .B(io_wide_out_15), .C(io_pmod_1_out_7), 
         .D(io_sdram_dq_out_10), .Z(n152)) /* synthesis lut_function=(A (B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i59_4_lut.init = 16'h8000;
    BB io_sdram_dq_pad_0 (.I(GND_net), .T(counter[0]), .B(io_sdram_dq[0]), 
       .O(io_sdram_dq_out_0));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(43[9:20])
    LUT4 i71_4_lut (.A(io_ft_data_out_1), .B(n142), .C(n96), .D(io_pmod_1_out_6), 
         .Z(n164)) /* synthesis lut_function=(A (B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i71_4_lut.init = 16'h8000;
    BB io_pmod_1_pad_7 (.I(GND_net), .T(counter[0]), .B(io_pmod_1[7]), 
       .O(io_pmod_1_out_7));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(45[9:18])
    LUT4 i47_3_lut (.A(io_ft_data_out_3), .B(io_ft_gpio1_c), .C(io_wide_out_12), 
         .Z(n140)) /* synthesis lut_function=(A (B (C))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i47_3_lut.init = 16'h8080;
    BB io_pmod_1_pad_6 (.I(GND_net), .T(counter[0]), .B(io_pmod_1[6]), 
       .O(io_pmod_1_out_6));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(45[9:18])
    BB io_pmod_1_pad_5 (.I(GND_net), .T(counter[0]), .B(io_pmod_1[5]), 
       .O(io_pmod_1_out_5));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(45[9:18])
    BB io_pmod_1_pad_4 (.I(GND_net), .T(counter[0]), .B(io_pmod_1[4]), 
       .O(io_pmod_1_out_4));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(45[9:18])
    LUT4 i54_4_lut (.A(io_wide_out_24), .B(io_wide_out_4), .C(io_pmod_2_out_0), 
         .D(io_sdram_dq_out_15), .Z(n147)) /* synthesis lut_function=(A (B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i54_4_lut.init = 16'h8000;
    BB io_pmod_1_pad_3 (.I(GND_net), .T(counter[0]), .B(io_pmod_1[3]), 
       .O(io_pmod_1_out_3));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(45[9:18])
    LUT4 i85_4_lut (.A(n115), .B(n170), .C(n152), .D(n116), .Z(n178)) /* synthesis lut_function=(A (B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i85_4_lut.init = 16'h8000;
    BB io_pmod_1_pad_2 (.I(GND_net), .T(counter[0]), .B(io_pmod_1[2]), 
       .O(io_pmod_1_out_2));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(45[9:18])
    BB io_pmod_1_pad_1 (.I(GND_net), .T(counter[0]), .B(io_pmod_1[1]), 
       .O(io_pmod_1_out_1));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(45[9:18])
    FD1S3IX counter_327__i24 (.D(n111), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(counter[24])) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i24.GSR = "ENABLED";
    BB io_pmod_1_pad_0 (.I(GND_net), .T(counter[0]), .B(io_pmod_1[0]), 
       .O(io_pmod_1_out_0));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(45[9:18])
    FD1S3IX counter_327__i23 (.D(n112_adj_1), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(counter[23])) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i23.GSR = "ENABLED";
    BB io_pmod_2_pad_7 (.I(GND_net), .T(counter[0]), .B(io_pmod_2[7]), 
       .O(io_pmod_2_out_7));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(46[9:18])
    FD1S3IX counter_327__i22 (.D(n113), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(counter[22])) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i22.GSR = "ENABLED";
    BB io_pmod_2_pad_6 (.I(GND_net), .T(counter[0]), .B(io_pmod_2[6]), 
       .O(io_pmod_2_out_6));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(46[9:18])
    FD1S3IX counter_327__i21 (.D(n114), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(counter[21])) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i21.GSR = "ENABLED";
    BB io_pmod_2_pad_5 (.I(GND_net), .T(counter[0]), .B(io_pmod_2[5]), 
       .O(io_pmod_2_out_5));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(46[9:18])
    FD1S3IX counter_327__i20 (.D(n115_adj_2), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(counter[20])) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i20.GSR = "ENABLED";
    BB io_pmod_2_pad_4 (.I(GND_net), .T(counter[0]), .B(io_pmod_2[4]), 
       .O(io_pmod_2_out_4));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(46[9:18])
    FD1S3IX counter_327__i19 (.D(n116_adj_3), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(counter[19])) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i19.GSR = "ENABLED";
    BB io_pmod_2_pad_3 (.I(GND_net), .T(counter[0]), .B(io_pmod_2[3]), 
       .O(io_pmod_2_out_3));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(46[9:18])
    FD1S3IX counter_327__i18 (.D(n117), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(counter[18])) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i18.GSR = "ENABLED";
    BB io_pmod_2_pad_2 (.I(GND_net), .T(counter[0]), .B(io_pmod_2[2]), 
       .O(io_pmod_2_out_2));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(46[9:18])
    FD1S3IX counter_327__i17 (.D(n118), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(n9)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i17.GSR = "ENABLED";
    BB io_pmod_2_pad_1 (.I(GND_net), .T(counter[0]), .B(io_pmod_2[1]), 
       .O(io_pmod_2_out_1));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(46[9:18])
    FD1S3IX counter_327__i16 (.D(n119), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(n10)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i16.GSR = "ENABLED";
    BB io_pmod_2_pad_0 (.I(GND_net), .T(counter[0]), .B(io_pmod_2[0]), 
       .O(io_pmod_2_out_0));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(46[9:18])
    FD1S3IX counter_327__i15 (.D(n120_adj_4), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(n11)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i15.GSR = "ENABLED";
    BB io_wide_pad_39 (.I(counter[25]), .T(counter[0]), .B(io_wide[39]), 
       .O(io_wide_out_39));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(39[9:16])
    FD1S3IX counter_327__i14 (.D(n121), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(n12)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i14.GSR = "ENABLED";
    BB io_wide_pad_38 (.I(counter[24]), .T(counter[0]), .B(io_wide[38]), 
       .O(io_wide_out_38));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(39[9:16])
    FD1S3IX counter_327__i13 (.D(n122), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(n13)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i13.GSR = "ENABLED";
    BB io_wide_pad_37 (.I(counter[23]), .T(counter[0]), .B(io_wide[37]), 
       .O(io_wide_out_37));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(39[9:16])
    FD1S3IX counter_327__i12 (.D(n123), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(n14)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i12.GSR = "ENABLED";
    BB io_wide_pad_36 (.I(counter[22]), .T(counter[0]), .B(io_wide[36]), 
       .O(io_wide_out_36));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(39[9:16])
    FD1S3IX counter_327__i11 (.D(n124_adj_5), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(n15)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i11.GSR = "ENABLED";
    BB io_wide_pad_35 (.I(counter[21]), .T(counter[0]), .B(io_wide[35]), 
       .O(io_wide_out_35));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(39[9:16])
    FD1S3IX counter_327__i10 (.D(n125), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(n16)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i10.GSR = "ENABLED";
    BB io_wide_pad_34 (.I(counter[20]), .T(counter[0]), .B(io_wide[34]), 
       .O(io_wide_out_34));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(39[9:16])
    FD1S3IX counter_327__i9 (.D(n126), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(n17)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i9.GSR = "ENABLED";
    BB io_wide_pad_33 (.I(counter[19]), .T(counter[0]), .B(io_wide[33]), 
       .O(io_wide_out_33));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(39[9:16])
    FD1S3IX counter_327__i8 (.D(n127), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(n18)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i8.GSR = "ENABLED";
    BB io_wide_pad_32 (.I(counter[18]), .T(counter[0]), .B(io_wide[32]), 
       .O(io_wide_out_32));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(39[9:16])
    FD1S3IX counter_327__i7 (.D(n128_adj_6), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(n19)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i7.GSR = "ENABLED";
    BB io_wide_pad_31 (.I(GND_net), .T(counter[0]), .B(io_wide[31]), .O(io_wide_out_31));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    FD1S3IX counter_327__i6 (.D(n129), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(n20)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i6.GSR = "ENABLED";
    BB io_wide_pad_30 (.I(GND_net), .T(counter[0]), .B(io_wide[30]), .O(io_wide_out_30));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    FD1S3IX counter_327__i5 (.D(n130), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(n21)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i5.GSR = "ENABLED";
    BB io_wide_pad_29 (.I(GND_net), .T(counter[0]), .B(io_wide[29]), .O(io_wide_out_29));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    FD1S3IX counter_327__i4 (.D(n131_adj_7), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(n22)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i4.GSR = "ENABLED";
    BB io_wide_pad_28 (.I(GND_net), .T(counter[0]), .B(io_wide[28]), .O(io_wide_out_28));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    FD1S3IX counter_327__i3 (.D(n132_adj_8), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(n23)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i3.GSR = "ENABLED";
    BB io_wide_pad_27 (.I(GND_net), .T(counter[0]), .B(io_wide[27]), .O(io_wide_out_27));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    FD1S3IX counter_327__i2 (.D(n133), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(n24)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i2.GSR = "ENABLED";
    BB io_wide_pad_26 (.I(GND_net), .T(counter[0]), .B(io_wide[26]), .O(io_wide_out_26));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    FD1S3IX counter_327__i1 (.D(n134), .CK(i_clk16_c), .CD(io_ft_gpio1_c), 
            .Q(n25)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327__i1.GSR = "ENABLED";
    BB io_wide_pad_25 (.I(GND_net), .T(counter[0]), .B(io_wide[25]), .O(io_wide_out_25));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    LUT4 i61_4_lut (.A(io_wide_out_29), .B(io_ft_data_out_7), .C(io_wide_out_18), 
         .D(i_ft_oe_n_c), .Z(n154)) /* synthesis lut_function=(A (B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i61_4_lut.init = 16'h8000;
    BB io_wide_pad_24 (.I(GND_net), .T(counter[0]), .B(io_wide[24]), .O(io_wide_out_24));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    LUT4 i75_4_lut (.A(io_wide_out_31), .B(n150), .C(n112), .D(io_ft_data_out_10), 
         .Z(n168)) /* synthesis lut_function=(A (B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i75_4_lut.init = 16'h8000;
    BB io_wide_pad_23 (.I(GND_net), .T(counter[0]), .B(io_wide[23]), .O(io_wide_out_23));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    LUT4 i55_4_lut (.A(io_wide_out_33), .B(io_wide_out_25), .C(io_wide_out_2), 
         .D(io_sdram_dq_out_2), .Z(n148)) /* synthesis lut_function=(A (B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i55_4_lut.init = 16'h8000;
    BB io_wide_pad_22 (.I(GND_net), .T(counter[0]), .B(io_wide[22]), .O(io_wide_out_22));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    LUT4 i49_4_lut (.A(io_sdram_dq_out_1), .B(io_ft_data_out_12), .C(io_wide_out_3), 
         .D(io_wide_out_9), .Z(n142)) /* synthesis lut_function=(A (B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i49_4_lut.init = 16'h8000;
    BB io_wide_pad_21 (.I(GND_net), .T(counter[0]), .B(io_wide[21]), .O(io_wide_out_21));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    LUT4 i3_2_lut (.A(io_ft_data_out_5), .B(i_ft_rd_n_c), .Z(n96)) /* synthesis lut_function=(A (B)) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i3_2_lut.init = 16'h8888;
    BB io_wide_pad_20 (.I(GND_net), .T(counter[0]), .B(io_wide[20]), .O(io_wide_out_20));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    LUT4 i38_2_lut (.A(io_pmod_2_out_2), .B(io_wide_out_22), .Z(n131)) /* synthesis lut_function=(A (B)) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i38_2_lut.init = 16'h8888;
    BB io_wide_pad_19 (.I(GND_net), .T(counter[0]), .B(io_wide[19]), .O(io_wide_out_19));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    LUT4 i81_4_lut (.A(io_pmod_2_out_1), .B(n162), .C(n136), .D(io_wide_out_32), 
         .Z(n174)) /* synthesis lut_function=(A (B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i81_4_lut.init = 16'h8000;
    BB io_wide_pad_18 (.I(GND_net), .T(counter[0]), .B(io_wide[18]), .O(io_wide_out_18));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    CCU2C counter_327_add_4_23 (.A0(counter[21]), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(counter[22]), .B1(GND_net), .C1(GND_net), 
          .D1(VCC_net), .CIN(n952), .COUT(n953), .S0(n114), .S1(n113));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327_add_4_23.INIT0 = 16'haaa0;
    defparam counter_327_add_4_23.INIT1 = 16'haaa0;
    defparam counter_327_add_4_23.INJECT1_0 = "NO";
    defparam counter_327_add_4_23.INJECT1_1 = "NO";
    BB io_wide_pad_17 (.I(GND_net), .T(counter[0]), .B(io_wide[17]), .O(io_wide_out_17));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    CCU2C counter_327_add_4_21 (.A0(counter[19]), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(counter[20]), .B1(GND_net), .C1(GND_net), 
          .D1(VCC_net), .CIN(n951), .COUT(n952), .S0(n116_adj_3), .S1(n115_adj_2));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327_add_4_21.INIT0 = 16'haaa0;
    defparam counter_327_add_4_21.INIT1 = 16'haaa0;
    defparam counter_327_add_4_21.INJECT1_0 = "NO";
    defparam counter_327_add_4_21.INJECT1_1 = "NO";
    BB io_wide_pad_16 (.I(GND_net), .T(counter[0]), .B(io_wide[16]), .O(io_wide_out_16));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    CCU2C counter_327_add_4_15 (.A0(n13), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n12), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n948), .COUT(n949), .S0(n122), .S1(n121));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327_add_4_15.INIT0 = 16'haaa0;
    defparam counter_327_add_4_15.INIT1 = 16'haaa0;
    defparam counter_327_add_4_15.INJECT1_0 = "NO";
    defparam counter_327_add_4_15.INJECT1_1 = "NO";
    BB io_wide_pad_15 (.I(GND_net), .T(counter[0]), .B(io_wide[15]), .O(io_wide_out_15));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    BB io_wide_pad_14 (.I(GND_net), .T(counter[0]), .B(io_wide[14]), .O(io_wide_out_14));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    LUT4 i27_2_lut (.A(io_wide_out_8), .B(io_ft_data_out_4), .Z(n120)) /* synthesis lut_function=(A (B)) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i27_2_lut.init = 16'h8888;
    BB io_wide_pad_13 (.I(GND_net), .T(counter[0]), .B(io_wide[13]), .O(io_wide_out_13));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    CCU2C counter_327_add_4_13 (.A0(n15), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n14), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n947), .COUT(n948), .S0(n124_adj_5), .S1(n123));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327_add_4_13.INIT0 = 16'haaa0;
    defparam counter_327_add_4_13.INIT1 = 16'haaa0;
    defparam counter_327_add_4_13.INJECT1_0 = "NO";
    defparam counter_327_add_4_13.INJECT1_1 = "NO";
    BB io_wide_pad_12 (.I(GND_net), .T(counter[0]), .B(io_wide[12]), .O(io_wide_out_12));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    CCU2C counter_327_add_4_27 (.A0(counter[25]), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(GND_net), .B1(GND_net), .C1(GND_net), .D1(GND_net), 
          .CIN(n954), .S0(n110));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327_add_4_27.INIT0 = 16'haaa0;
    defparam counter_327_add_4_27.INIT1 = 16'h0000;
    defparam counter_327_add_4_27.INJECT1_0 = "NO";
    defparam counter_327_add_4_27.INJECT1_1 = "NO";
    BB io_wide_pad_11 (.I(GND_net), .T(counter[0]), .B(io_wide[11]), .O(io_wide_out_11));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    LUT4 i67_4_lut (.A(io_pmod_1_out_0), .B(io_sdram_dq_out_4), .C(io_wide_out_17), 
         .D(io_wide_out_37), .Z(n160)) /* synthesis lut_function=(A (B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i67_4_lut.init = 16'h8000;
    BB io_wide_pad_10 (.I(GND_net), .T(counter[0]), .B(io_wide[10]), .O(io_wide_out_10));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    CCU2C counter_327_add_4_11 (.A0(n17), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n16), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n946), .COUT(n947), .S0(n126), .S1(n125));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327_add_4_11.INIT0 = 16'haaa0;
    defparam counter_327_add_4_11.INIT1 = 16'haaa0;
    defparam counter_327_add_4_11.INJECT1_0 = "NO";
    defparam counter_327_add_4_11.INJECT1_1 = "NO";
    BB io_wide_pad_9 (.I(GND_net), .T(counter[0]), .B(io_wide[9]), .O(io_wide_out_9));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    CCU2C counter_327_add_4_9 (.A0(n19), .B0(GND_net), .C0(GND_net), .D0(VCC_net), 
          .A1(n18), .B1(GND_net), .C1(GND_net), .D1(VCC_net), .CIN(n945), 
          .COUT(n946), .S0(n128_adj_6), .S1(n127));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327_add_4_9.INIT0 = 16'haaa0;
    defparam counter_327_add_4_9.INIT1 = 16'haaa0;
    defparam counter_327_add_4_9.INJECT1_0 = "NO";
    defparam counter_327_add_4_9.INJECT1_1 = "NO";
    BB io_wide_pad_8 (.I(GND_net), .T(counter[0]), .B(io_wide[8]), .O(io_wide_out_8));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    CCU2C counter_327_add_4_7 (.A0(n21), .B0(GND_net), .C0(GND_net), .D0(VCC_net), 
          .A1(n20), .B1(GND_net), .C1(GND_net), .D1(VCC_net), .CIN(n944), 
          .COUT(n945), .S0(n130), .S1(n129));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327_add_4_7.INIT0 = 16'haaa0;
    defparam counter_327_add_4_7.INIT1 = 16'haaa0;
    defparam counter_327_add_4_7.INJECT1_0 = "NO";
    defparam counter_327_add_4_7.INJECT1_1 = "NO";
    BB io_wide_pad_7 (.I(GND_net), .T(counter[0]), .B(io_wide[7]), .O(io_wide_out_7));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    CCU2C counter_327_add_4_5 (.A0(n23), .B0(GND_net), .C0(GND_net), .D0(VCC_net), 
          .A1(n22), .B1(GND_net), .C1(GND_net), .D1(VCC_net), .CIN(n943), 
          .COUT(n944), .S0(n132_adj_8), .S1(n131_adj_7));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327_add_4_5.INIT0 = 16'haaa0;
    defparam counter_327_add_4_5.INIT1 = 16'haaa0;
    defparam counter_327_add_4_5.INJECT1_0 = "NO";
    defparam counter_327_add_4_5.INJECT1_1 = "NO";
    BB io_wide_pad_6 (.I(GND_net), .T(counter[0]), .B(io_wide[6]), .O(io_wide_out_6));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    CCU2C counter_327_add_4_3 (.A0(n25), .B0(GND_net), .C0(GND_net), .D0(VCC_net), 
          .A1(n24), .B1(GND_net), .C1(GND_net), .D1(VCC_net), .CIN(n942), 
          .COUT(n943), .S0(n134), .S1(n133));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327_add_4_3.INIT0 = 16'haaa0;
    defparam counter_327_add_4_3.INIT1 = 16'haaa0;
    defparam counter_327_add_4_3.INJECT1_0 = "NO";
    defparam counter_327_add_4_3.INJECT1_1 = "NO";
    BB io_wide_pad_5 (.I(GND_net), .T(counter[0]), .B(io_wide[5]), .O(io_wide_out_5));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    CCU2C counter_327_add_4_1 (.A0(GND_net), .B0(GND_net), .C0(GND_net), 
          .D0(GND_net), .A1(counter[0]), .B1(GND_net), .C1(GND_net), 
          .D1(VCC_net), .COUT(n942), .S1(n135));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327_add_4_1.INIT0 = 16'h0000;
    defparam counter_327_add_4_1.INIT1 = 16'h555f;
    defparam counter_327_add_4_1.INJECT1_0 = "NO";
    defparam counter_327_add_4_1.INJECT1_1 = "NO";
    BB io_wide_pad_4 (.I(GND_net), .T(counter[0]), .B(io_wide[4]), .O(io_wide_out_4));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    CCU2C counter_327_add_4_19 (.A0(n9), .B0(GND_net), .C0(GND_net), .D0(VCC_net), 
          .A1(counter[18]), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n950), .COUT(n951), .S0(n118), .S1(n117));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327_add_4_19.INIT0 = 16'haaa0;
    defparam counter_327_add_4_19.INIT1 = 16'haaa0;
    defparam counter_327_add_4_19.INJECT1_0 = "NO";
    defparam counter_327_add_4_19.INJECT1_1 = "NO";
    BB io_wide_pad_3 (.I(GND_net), .T(counter[0]), .B(io_wide[3]), .O(io_wide_out_3));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    LUT4 i39_2_lut (.A(io_pmod_2_out_6), .B(io_wide_out_5), .Z(n132)) /* synthesis lut_function=(A (B)) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i39_2_lut.init = 16'h8888;
    BB io_wide_pad_2 (.I(GND_net), .T(counter[0]), .B(io_wide[2]), .O(io_wide_out_2));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    BB io_wide_pad_1 (.I(GND_net), .T(counter[0]), .B(io_wide[1]), .O(io_wide_out_1));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    CCU2C counter_327_add_4_17 (.A0(n11), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n10), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n949), .COUT(n950), .S0(n120_adj_4), .S1(n119));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327_add_4_17.INIT0 = 16'haaa0;
    defparam counter_327_add_4_17.INIT1 = 16'haaa0;
    defparam counter_327_add_4_17.INJECT1_0 = "NO";
    defparam counter_327_add_4_17.INJECT1_1 = "NO";
    BB io_wide_pad_0 (.I(GND_net), .T(counter[0]), .B(io_wide[0]), .O(io_wide_out_0));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(41[9:16])
    CCU2C counter_327_add_4_25 (.A0(counter[23]), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(counter[24]), .B1(GND_net), .C1(GND_net), 
          .D1(VCC_net), .CIN(n953), .COUT(n954), .S0(n112_adj_1), .S1(n111));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(67[15:26])
    defparam counter_327_add_4_25.INIT0 = 16'haaa0;
    defparam counter_327_add_4_25.INIT1 = 16'haaa0;
    defparam counter_327_add_4_25.INJECT1_0 = "NO";
    defparam counter_327_add_4_25.INJECT1_1 = "NO";
    OB i_ft_be_pad_1 (.I(GND_net), .O(i_ft_be[1]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(9[21:28])
    OB i_ft_be_pad_0 (.I(GND_net), .O(i_ft_be[0]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(9[21:28])
    OB i_ft_txe_n_pad (.I(GND_net), .O(i_ft_txe_n));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(10[21:31])
    OB i_ft_rxf_n_pad (.I(GND_net), .O(i_ft_rxf_n));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(11[21:31])
    OB o_sdram_dqm_pad_1 (.I(GND_net), .O(o_sdram_dqm[1]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(19[21:32])
    OB o_sdram_dqm_pad_0 (.I(GND_net), .O(o_sdram_dqm[0]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(19[21:32])
    OB o_sdram_a_pad_12 (.I(GND_net), .O(o_sdram_a[12]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(20[21:30])
    OB o_sdram_a_pad_11 (.I(GND_net), .O(o_sdram_a[11]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(20[21:30])
    OB o_sdram_a_pad_10 (.I(GND_net), .O(o_sdram_a[10]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(20[21:30])
    OB o_sdram_a_pad_9 (.I(GND_net), .O(o_sdram_a[9]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(20[21:30])
    OB o_sdram_a_pad_8 (.I(GND_net), .O(o_sdram_a[8]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(20[21:30])
    OB o_sdram_a_pad_7 (.I(GND_net), .O(o_sdram_a[7]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(20[21:30])
    OB o_sdram_a_pad_6 (.I(GND_net), .O(o_sdram_a[6]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(20[21:30])
    OB o_sdram_a_pad_5 (.I(GND_net), .O(o_sdram_a[5]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(20[21:30])
    OB o_sdram_a_pad_4 (.I(GND_net), .O(o_sdram_a[4]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(20[21:30])
    OB o_sdram_a_pad_3 (.I(GND_net), .O(o_sdram_a[3]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(20[21:30])
    OB o_sdram_a_pad_2 (.I(GND_net), .O(o_sdram_a[2]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(20[21:30])
    OB o_sdram_a_pad_1 (.I(GND_net), .O(o_sdram_a[1]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(20[21:30])
    OB o_sdram_a_pad_0 (.I(GND_net), .O(o_sdram_a[0]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(20[21:30])
    OB o_sdram_ba_pad_1 (.I(GND_net), .O(o_sdram_ba[1]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(21[21:31])
    OB o_sdram_ba_pad_0 (.I(GND_net), .O(o_sdram_ba[0]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(21[21:31])
    OB o_sdram_cs_n_pad (.I(GND_net), .O(o_sdram_cs_n));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(22[21:33])
    OB o_sdram_ras_n_pad (.I(GND_net), .O(o_sdram_ras_n));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(23[21:34])
    OB o_sdram_cas_n_pad (.I(GND_net), .O(o_sdram_cas_n));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(24[21:34])
    OB o_sdram_we_n_pad (.I(GND_net), .O(o_sdram_we_n));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(25[21:33])
    OB o_sdram_clk_n_pad (.I(GND_net), .O(o_sdram_clk_n));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(26[21:34])
    OB o_sdram_cke_n_pad (.I(GND_net), .O(o_sdram_cke_n));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(27[21:34])
    OBZ io_pmod_0_pad_7 (.I(GND_net), .T(io_pmod_0_7__N_2), .O(io_pmod_0[7]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[9:18])
    OBZ io_pmod_0_pad_6 (.I(GND_net), .T(io_pmod_0_7__N_2), .O(io_pmod_0[6]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[9:18])
    LUT4 i57_4_lut (.A(io_ft_data_out_15), .B(io_sdram_dq_out_7), .C(io_pmod_1_out_3), 
         .D(io_wide_out_13), .Z(n150)) /* synthesis lut_function=(A (B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i57_4_lut.init = 16'h8000;
    OBZ io_pmod_0_pad_5 (.I(GND_net), .T(io_pmod_0_7__N_2), .O(io_pmod_0[5]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[9:18])
    LUT4 i69_4_lut (.A(io_sdram_dq_out_11), .B(io_wide_out_0), .C(io_sdram_dq_out_12), 
         .D(io_sdram_dq_out_14), .Z(n162)) /* synthesis lut_function=(A (B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i69_4_lut.init = 16'h8000;
    OBZ io_pmod_0_pad_4 (.I(GND_net), .T(io_pmod_0_7__N_2), .O(io_pmod_0[4]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[9:18])
    LUT4 i43_2_lut (.A(io_wide_out_19), .B(io_ft_data_out_2), .Z(n136)) /* synthesis lut_function=(A (B)) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i43_2_lut.init = 16'h8888;
    OBZ io_pmod_0_pad_3 (.I(GND_net), .T(io_pmod_0_7__N_2), .O(io_pmod_0[3]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[9:18])
    OBZ io_pmod_0_pad_2 (.I(GND_net), .T(io_pmod_0_7__N_2), .O(io_pmod_0[2]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[9:18])
    LUT4 i19_2_lut (.A(io_ft_data_out_13), .B(io_sdram_dq_out_6), .Z(n112)) /* synthesis lut_function=(A (B)) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i19_2_lut.init = 16'h8888;
    OBZ io_pmod_0_pad_1 (.I(GND_net), .T(io_pmod_0_7__N_2), .O(io_pmod_0[1]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[9:18])
    LUT4 i65_4_lut (.A(i_ft_clk_c), .B(io_ft_data_out_11), .C(io_wide_out_16), 
         .D(io_sdram_dq_out_9), .Z(n158)) /* synthesis lut_function=(A (B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[21] 60[4])
    defparam i65_4_lut.init = 16'h8000;
    OBZ io_pmod_0_pad_0 (.I(VCC_net), .T(io_pmod_0_7__N_2), .O(io_pmod_0[0]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(49[9:18])
    GSR GSR_INST (.GSR(VCC_net));
    IB i_clk16_pad (.I(i_clk16), .O(i_clk16_c));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(4[13:20])
    IB i_ft_clk_pad (.I(i_ft_clk), .O(i_ft_clk_c));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(8[21:29])
    IB i_ft_wr_n_pad (.I(i_ft_wr_n), .O(i_ft_wr_n_c));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(12[21:30])
    IB i_ft_rd_n_pad (.I(i_ft_rd_n), .O(i_ft_rd_n_c));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(13[21:30])
    IB i_ft_oe_n_pad (.I(i_ft_oe_n), .O(i_ft_oe_n_c));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(14[21:30])
    IB io_ft_gpio1_pad (.I(io_ft_gpio1), .O(io_ft_gpio1_c));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(15[21:32])
    
endmodule
//
// Verilog Description of module PUR
// module not written out since it is a black-box. 
//

