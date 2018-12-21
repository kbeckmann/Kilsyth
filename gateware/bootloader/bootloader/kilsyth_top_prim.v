// Verilog netlist produced by program LSE :  version Diamond (64-bit) 3.10.3.144.3
// Netlist written on Fri Dec 21 01:39:43 2018
//
// Verilog Description of module kilsyth_top
//

module kilsyth_top (i_clk16, io_ft_data, i_ft_clk, io_ft_be, i_ft_txe_n, 
            i_ft_rxf_n, o_ft_wr_n, o_ft_rd_n, io_ft_oe_n, io_ft_gpio1, 
            o_leds) /* synthesis syn_module_defined=1 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(3[8:19])
    input i_clk16;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(4[13:20])
    output [15:0]io_ft_data;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(7[21:31])
    input i_ft_clk;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(8[21:29])
    inout [1:0]io_ft_be;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(9[21:29])
    input i_ft_txe_n;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(10[21:31])
    input i_ft_rxf_n;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(11[21:31])
    output o_ft_wr_n;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(12[21:30])
    output o_ft_rd_n;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(13[21:30])
    output io_ft_oe_n /* synthesis .original_dir=IN_OUT */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(14[21:31])
    input io_ft_gpio1 /* synthesis .original_dir=IN_OUT */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(15[21:32])
    output [7:0]o_leds;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(40[19:25])
    
    wire GND_net /* synthesis RESET_NET_FOR_BUS20=20, DSPPORT_20=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(55[13:24])
    wire VCC_net /* synthesis CE_NET_FOR_BUS20=20, DSPPORT_20=CE3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(59[12:17])
    wire i_clk16_c /* synthesis DSPPORT_20=CLK3, CLOCK_NET_FOR_BUS20=20, is_clock=1, SET_AS_NETWORK=i_clk16_c */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(4[13:20])
    wire i_ft_clk_c /* synthesis is_clock=1, SET_AS_NETWORK=i_ft_clk_c */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(8[21:29])
    
    wire i_ft_txe_n_c, i_ft_rxf_n_c, o_ft_wr_n_c, o_ft_rd_n_c, io_ft_oe_n_c, 
        o_leds_c_7, o_leds_c_6, o_leds_c_5, o_leds_c_4, o_leds_c_3, 
        o_leds_c_2, o_leds_c_1, o_leds_c_0;
    wire [25:0]counter;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(43[13:20])
    
    wire n22, n21, n20, n1338;
    wire [15:0]ft_data_buf;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(55[13:24])
    
    wire n1341, n1340, ft_data_dir;
    wire [7:0]state;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(72[12:17])
    wire [7:0]next_state;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(73[12:22])
    
    wire wants_to_write, n753, o_leds_6__N_2, n1337, wants_to_write_N_87, 
        n1339, n1032, n1336, n1335, n1334, n19, n1333, i_ft_clk_c_enable_9, 
        i_ft_clk_c_enable_4, n1332, n125, n124, n123, n122, n24, 
        n23, n102, n121, n120, n119, n118, n1380, n18, n17, 
        n117, n116, n115, n114, n113, n16, n15, n1158, n112, 
        n111, n110, n109, n1360, io_ft_be_out_0, n1377, n108, 
        n107, n106, n105, n14, n13, n1343, n12, n11, n10, 
        n9, n8, n7, n6, n1342, n1385, n1382, n1384, i_ft_clk_c_enable_6, 
        n1381, n5, n1383, io_ft_be_out_1, n4, n3, n104, n103, 
        i_ft_clk_c_enable_3, n1356, n1378, n2, i_ft_clk_c_enable_7;
    
    VHI i2 (.Z(VCC_net));
    FD1S3AX leds_4__116 (.D(i_ft_rxf_n_c), .CK(i_clk16_c), .Q(o_leds_c_4)) /* synthesis lse_init_val=0 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(63[9] 70[5])
    defparam leds_4__116.GSR = "ENABLED";
    FD1S3AX leds_3__117 (.D(i_ft_txe_n_c), .CK(i_clk16_c), .Q(o_leds_c_3)) /* synthesis lse_init_val=0 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(63[9] 70[5])
    defparam leds_3__117.GSR = "ENABLED";
    FD1S3AX leds_2__118 (.D(io_ft_be_out_1), .CK(i_clk16_c), .Q(o_leds_c_2)) /* synthesis lse_init_val=0 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(63[9] 70[5])
    defparam leds_2__118.GSR = "ENABLED";
    FD1S3AX leds_1__119 (.D(io_ft_be_out_0), .CK(i_clk16_c), .Q(o_leds_c_1)) /* synthesis lse_init_val=0 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(63[9] 70[5])
    defparam leds_1__119.GSR = "ENABLED";
    FD1S3AX leds_0__120 (.D(counter[23]), .CK(i_clk16_c), .Q(o_leds_c_0)) /* synthesis lse_init_val=0 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(63[9] 70[5])
    defparam leds_0__120.GSR = "ENABLED";
    FD1S3AX leds_7__121 (.D(wants_to_write), .CK(i_ft_clk_c), .Q(o_leds_c_7)) /* synthesis lse_init_val=0 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(83[9] 140[5])
    defparam leds_7__121.GSR = "ENABLED";
    FD1S3AX state_i0 (.D(next_state[0]), .CK(i_ft_clk_c), .Q(state[0])) /* synthesis lse_init_val=0 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(83[9] 140[5])
    defparam state_i0.GSR = "ENABLED";
    LUT4 next_state_7__N_60_1__bdd_3_lut_513 (.A(state[2]), .B(i_ft_rxf_n_c), 
         .C(state[1]), .Z(n1377)) /* synthesis lut_function=(!(A+!(B+(C)))) */ ;
    defparam next_state_7__N_60_1__bdd_3_lut_513.init = 16'h5454;
    FD1S3AX leds_6__122 (.D(o_leds_6__N_2), .CK(i_ft_clk_c), .Q(o_leds_c_6)) /* synthesis lse_init_val=0 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(83[9] 140[5])
    defparam leds_6__122.GSR = "ENABLED";
    FD1P3AY ft_oe_n_124 (.D(n753), .SP(i_ft_clk_c_enable_3), .CK(i_ft_clk_c), 
            .Q(io_ft_oe_n_c)) /* synthesis lse_init_val=1 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(83[9] 140[5])
    defparam ft_oe_n_124.GSR = "ENABLED";
    FD1P3AY ft_wr_n_126 (.D(n1382), .SP(i_ft_clk_c_enable_3), .CK(i_ft_clk_c), 
            .Q(o_ft_wr_n_c)) /* synthesis lse_init_val=1 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(83[9] 140[5])
    defparam ft_wr_n_126.GSR = "ENABLED";
    FD1P3AX ft_data_dir_127 (.D(n1381), .SP(i_ft_clk_c_enable_3), .CK(i_ft_clk_c), 
            .Q(ft_data_dir)) /* synthesis lse_init_val=0 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(83[9] 140[5])
    defparam ft_data_dir_127.GSR = "ENABLED";
    FD1P3AX wants_to_write_128 (.D(n1356), .SP(i_ft_clk_c_enable_4), .CK(i_ft_clk_c), 
            .Q(wants_to_write)) /* synthesis lse_init_val=0 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(83[9] 140[5])
    defparam wants_to_write_128.GSR = "ENABLED";
    FD1P3IX next_state__i0 (.D(n1384), .SP(i_ft_clk_c_enable_9), .CD(n1032), 
            .CK(i_ft_clk_c), .Q(next_state[0])) /* synthesis lse_init_val=0 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(83[9] 140[5])
    defparam next_state__i0.GSR = "ENABLED";
    CCU2C counter_296_302_add_4_17 (.A0(n9), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n8), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n1339), .COUT(n1340), .S0(n110), .S1(n109));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302_add_4_17.INIT0 = 16'haaa0;
    defparam counter_296_302_add_4_17.INIT1 = 16'haaa0;
    defparam counter_296_302_add_4_17.INJECT1_0 = "NO";
    defparam counter_296_302_add_4_17.INJECT1_1 = "NO";
    LUT4 i308_1_lut (.A(ft_data_dir), .Z(n1158)) /* synthesis lut_function=(!(A)) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(60[9:17])
    defparam i308_1_lut.init = 16'h5555;
    CCU2C counter_296_302_add_4_15 (.A0(n11), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n10), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n1338), .COUT(n1339), .S0(n112), .S1(n111));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302_add_4_15.INIT0 = 16'haaa0;
    defparam counter_296_302_add_4_15.INIT1 = 16'haaa0;
    defparam counter_296_302_add_4_15.INJECT1_0 = "NO";
    defparam counter_296_302_add_4_15.INJECT1_1 = "NO";
    CCU2C counter_296_302_add_4_13 (.A0(n13), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n12), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n1337), .COUT(n1338), .S0(n114), .S1(n113));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302_add_4_13.INIT0 = 16'haaa0;
    defparam counter_296_302_add_4_13.INIT1 = 16'haaa0;
    defparam counter_296_302_add_4_13.INJECT1_0 = "NO";
    defparam counter_296_302_add_4_13.INJECT1_1 = "NO";
    FD1S3AX counter_296_302__i0 (.D(n125), .CK(i_clk16_c), .Q(n24)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302__i0.GSR = "ENABLED";
    LUT4 i330_2_lut (.A(i_ft_txe_n_c), .B(wants_to_write), .Z(wants_to_write_N_87)) /* synthesis lut_function=(A (B)) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(98[14] 104[8])
    defparam i330_2_lut.init = 16'h8888;
    FD1P3AX ft_rd_n_125 (.D(n1380), .SP(i_ft_clk_c_enable_6), .CK(i_ft_clk_c), 
            .Q(o_ft_rd_n_c));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(83[9] 140[5])
    defparam ft_rd_n_125.GSR = "ENABLED";
    CCU2C counter_296_302_add_4_11 (.A0(n15), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n14), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n1336), .COUT(n1337), .S0(n116), .S1(n115));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302_add_4_11.INIT0 = 16'haaa0;
    defparam counter_296_302_add_4_11.INIT1 = 16'haaa0;
    defparam counter_296_302_add_4_11.INJECT1_0 = "NO";
    defparam counter_296_302_add_4_11.INJECT1_1 = "NO";
    LUT4 i1_4_lut_4_lut (.A(state[1]), .B(i_ft_rxf_n_c), .C(state[0]), 
         .D(state[2]), .Z(i_ft_clk_c_enable_4)) /* synthesis lut_function=(!(A+(B (C (D))+!B (C)))) */ ;
    defparam i1_4_lut_4_lut.init = 16'h0545;
    CCU2C counter_296_302_add_4_9 (.A0(n17), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n16), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n1335), .COUT(n1336), .S0(n118), .S1(n117));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302_add_4_9.INIT0 = 16'haaa0;
    defparam counter_296_302_add_4_9.INIT1 = 16'haaa0;
    defparam counter_296_302_add_4_9.INJECT1_0 = "NO";
    defparam counter_296_302_add_4_9.INJECT1_1 = "NO";
    BB io_ft_be_pad_1 (.I(VCC_net), .T(n1158), .B(io_ft_be[1]), .O(io_ft_be_out_1));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(60[9:17])
    CCU2C counter_296_302_add_4_7 (.A0(n19), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n18), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n1334), .COUT(n1335), .S0(n120), .S1(n119));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302_add_4_7.INIT0 = 16'haaa0;
    defparam counter_296_302_add_4_7.INIT1 = 16'haaa0;
    defparam counter_296_302_add_4_7.INJECT1_0 = "NO";
    defparam counter_296_302_add_4_7.INJECT1_1 = "NO";
    LUT4 i2_3_lut_3_lut (.A(state[1]), .B(state[2]), .C(state[0]), .Z(n1032)) /* synthesis lut_function=(!(A+((C)+!B))) */ ;
    defparam i2_3_lut_3_lut.init = 16'h0404;
    CCU2C counter_296_302_add_4_5 (.A0(n21), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n20), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n1333), .COUT(n1334), .S0(n122), .S1(n121));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302_add_4_5.INIT0 = 16'haaa0;
    defparam counter_296_302_add_4_5.INIT1 = 16'haaa0;
    defparam counter_296_302_add_4_5.INJECT1_0 = "NO";
    defparam counter_296_302_add_4_5.INJECT1_1 = "NO";
    CCU2C counter_296_302_add_4_3 (.A0(n23), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n22), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n1332), .COUT(n1333), .S0(n124), .S1(n123));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302_add_4_3.INIT0 = 16'haaa0;
    defparam counter_296_302_add_4_3.INIT1 = 16'haaa0;
    defparam counter_296_302_add_4_3.INJECT1_0 = "NO";
    defparam counter_296_302_add_4_3.INJECT1_1 = "NO";
    LUT4 o_ft_rd_n_I_1_2_lut_rep_11 (.A(i_ft_txe_n_c), .B(wants_to_write), 
         .Z(n1383)) /* synthesis lut_function=(!(A+!(B))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(95[9:38])
    defparam o_ft_rd_n_I_1_2_lut_rep_11.init = 16'h4444;
    LUT4 i467_2_lut_rep_8_3_lut (.A(i_ft_txe_n_c), .B(wants_to_write), .C(i_ft_rxf_n_c), 
         .Z(n1380)) /* synthesis lut_function=(A (C)+!A (B+(C))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(95[9:38])
    defparam i467_2_lut_rep_8_3_lut.init = 16'hf4f4;
    LUT4 next_state_7__N_60_1__bdd_3_lut_3_lut_4_lut (.A(i_ft_txe_n_c), .B(wants_to_write), 
         .C(i_ft_rxf_n_c), .D(state[1]), .Z(n1378)) /* synthesis lut_function=(!(A (C+(D))+!A (B (D)+!B (C+(D))))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(95[9:38])
    defparam next_state_7__N_60_1__bdd_3_lut_3_lut_4_lut.init = 16'h004f;
    LUT4 i1_3_lut (.A(state[2]), .B(state[1]), .C(state[0]), .Z(i_ft_clk_c_enable_3)) /* synthesis lut_function=(!(A+!(B (C)+!B !(C)))) */ ;
    defparam i1_3_lut.init = 16'h4141;
    CCU2C counter_296_302_add_4_1 (.A0(GND_net), .B0(GND_net), .C0(GND_net), 
          .D0(GND_net), .A1(n24), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .COUT(n1332), .S1(n125));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302_add_4_1.INIT0 = 16'h0000;
    defparam counter_296_302_add_4_1.INIT1 = 16'h555f;
    defparam counter_296_302_add_4_1.INJECT1_0 = "NO";
    defparam counter_296_302_add_4_1.INJECT1_1 = "NO";
    LUT4 mux_184_Mux_0_i3_3_lut_4_lut (.A(i_ft_rxf_n_c), .B(n1383), .C(state[1]), 
         .D(state[0]), .Z(n753)) /* synthesis lut_function=(A ((D)+!C)+!A (B ((D)+!C)+!B (C (D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(98[14] 104[8])
    defparam mux_184_Mux_0_i3_3_lut_4_lut.init = 16'hfe0e;
    FD1P3AX ft_data_buf__i1 (.D(n1385), .SP(i_ft_clk_c_enable_7), .CK(i_ft_clk_c), 
            .Q(ft_data_buf[7])) /* synthesis lse_init_val=0 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(83[9] 140[5])
    defparam ft_data_buf__i1.GSR = "ENABLED";
    FD1S3AX counter_296_302__i23 (.D(n102), .CK(i_clk16_c), .Q(counter[23])) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302__i23.GSR = "ENABLED";
    LUT4 i2_4_lut_4_lut (.A(state[1]), .B(state[0]), .C(wants_to_write_N_87), 
         .D(state[2]), .Z(n1356)) /* synthesis lut_function=(!(A+(B (D)+!B ((D)+!C)))) */ ;
    defparam i2_4_lut_4_lut.init = 16'h0054;
    FD1S3AX leds_5__115 (.D(o_ft_rd_n_c), .CK(i_clk16_c), .Q(o_leds_c_5)) /* synthesis lse_init_val=0 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(63[9] 70[5])
    defparam leds_5__115.GSR = "ENABLED";
    LUT4 i512_2_lut_rep_12 (.A(state[0]), .B(state[1]), .Z(n1384)) /* synthesis lut_function=(!(A+(B))) */ ;
    defparam i512_2_lut_rep_12.init = 16'h1111;
    LUT4 i1_2_lut_rep_9 (.A(state[1]), .B(state[0]), .Z(n1381)) /* synthesis lut_function=(A (B)) */ ;
    defparam i1_2_lut_rep_9.init = 16'h8888;
    LUT4 i2_1_lut_rep_10 (.A(state[1]), .Z(n1382)) /* synthesis lut_function=(!(A)) */ ;
    defparam i2_1_lut_rep_10.init = 16'h5555;
    LUT4 o_leds_6__I_0_1_lut (.A(o_leds_c_6), .Z(o_leds_6__N_2)) /* synthesis lut_function=(!(A)) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(84[17:25])
    defparam o_leds_6__I_0_1_lut.init = 16'h5555;
    FD1S3AX counter_296_302__i22 (.D(n103), .CK(i_clk16_c), .Q(n2)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302__i22.GSR = "ENABLED";
    FD1S3AX counter_296_302__i21 (.D(n104), .CK(i_clk16_c), .Q(n3)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302__i21.GSR = "ENABLED";
    FD1S3AX counter_296_302__i20 (.D(n105), .CK(i_clk16_c), .Q(n4)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302__i20.GSR = "ENABLED";
    FD1S3AX counter_296_302__i19 (.D(n106), .CK(i_clk16_c), .Q(n5)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302__i19.GSR = "ENABLED";
    FD1S3AX counter_296_302__i18 (.D(n107), .CK(i_clk16_c), .Q(n6)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302__i18.GSR = "ENABLED";
    FD1S3AX counter_296_302__i17 (.D(n108), .CK(i_clk16_c), .Q(n7)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302__i17.GSR = "ENABLED";
    FD1S3AX counter_296_302__i16 (.D(n109), .CK(i_clk16_c), .Q(n8)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302__i16.GSR = "ENABLED";
    FD1S3AX counter_296_302__i15 (.D(n110), .CK(i_clk16_c), .Q(n9)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302__i15.GSR = "ENABLED";
    FD1S3AX counter_296_302__i14 (.D(n111), .CK(i_clk16_c), .Q(n10)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302__i14.GSR = "ENABLED";
    FD1S3AX counter_296_302__i13 (.D(n112), .CK(i_clk16_c), .Q(n11)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302__i13.GSR = "ENABLED";
    FD1S3AX counter_296_302__i12 (.D(n113), .CK(i_clk16_c), .Q(n12)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302__i12.GSR = "ENABLED";
    FD1S3AX counter_296_302__i11 (.D(n114), .CK(i_clk16_c), .Q(n13)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302__i11.GSR = "ENABLED";
    FD1S3AX counter_296_302__i10 (.D(n115), .CK(i_clk16_c), .Q(n14)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302__i10.GSR = "ENABLED";
    FD1S3AX counter_296_302__i9 (.D(n116), .CK(i_clk16_c), .Q(n15)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302__i9.GSR = "ENABLED";
    LUT4 i22_3_lut_4_lut_3_lut (.A(state[0]), .B(state[1]), .C(state[2]), 
         .Z(i_ft_clk_c_enable_7)) /* synthesis lut_function=(!(A ((C)+!B)+!A (B+!(C)))) */ ;
    defparam i22_3_lut_4_lut_3_lut.init = 16'h1818;
    LUT4 i509_3_lut (.A(state[1]), .B(state[2]), .C(state[0]), .Z(i_ft_clk_c_enable_6)) /* synthesis lut_function=(!(A+(B+(C)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(88[3] 139[10])
    defparam i509_3_lut.init = 16'h0101;
    FD1S3AX counter_296_302__i8 (.D(n117), .CK(i_clk16_c), .Q(n16)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302__i8.GSR = "ENABLED";
    FD1S3AX counter_296_302__i7 (.D(n118), .CK(i_clk16_c), .Q(n17)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302__i7.GSR = "ENABLED";
    FD1S3AX counter_296_302__i6 (.D(n119), .CK(i_clk16_c), .Q(n18)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302__i6.GSR = "ENABLED";
    FD1S3AX counter_296_302__i5 (.D(n120), .CK(i_clk16_c), .Q(n19)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302__i5.GSR = "ENABLED";
    FD1S3AX counter_296_302__i4 (.D(n121), .CK(i_clk16_c), .Q(n20)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302__i4.GSR = "ENABLED";
    FD1S3AX counter_296_302__i3 (.D(n122), .CK(i_clk16_c), .Q(n21)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302__i3.GSR = "ENABLED";
    FD1S3AX counter_296_302__i2 (.D(n123), .CK(i_clk16_c), .Q(n22)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302__i2.GSR = "ENABLED";
    FD1S3AX counter_296_302__i1 (.D(n124), .CK(i_clk16_c), .Q(n23)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302__i1.GSR = "ENABLED";
    FD1P3IX next_state__i2 (.D(n1381), .SP(i_ft_clk_c_enable_9), .CD(n1032), 
            .CK(i_ft_clk_c), .Q(next_state[2])) /* synthesis lse_init_val=0 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(83[9] 140[5])
    defparam next_state__i2.GSR = "ENABLED";
    PFUMX i514 (.BLUT(n1378), .ALUT(n1377), .C0(state[0]), .Z(i_ft_clk_c_enable_9));
    LUT4 i4_1_lut_rep_13 (.A(state[0]), .Z(n1385)) /* synthesis lut_function=(!(A)) */ ;
    defparam i4_1_lut_rep_13.init = 16'h5555;
    FD1P3IX next_state__i1 (.D(n1360), .SP(i_ft_clk_c_enable_9), .CD(n1032), 
            .CK(i_ft_clk_c), .Q(next_state[1])) /* synthesis lse_init_val=0 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(83[9] 140[5])
    defparam next_state__i1.GSR = "ENABLED";
    FD1S3AX state_i2 (.D(next_state[2]), .CK(i_ft_clk_c), .Q(state[2])) /* synthesis lse_init_val=0 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(83[9] 140[5])
    defparam state_i2.GSR = "ENABLED";
    GSR GSR_INST (.GSR(VCC_net));
    FD1S3AX state_i1 (.D(next_state[1]), .CK(i_ft_clk_c), .Q(state[1])) /* synthesis lse_init_val=0 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(83[9] 140[5])
    defparam state_i1.GSR = "ENABLED";
    CCU2C counter_296_302_add_4_19 (.A0(n7), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n6), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n1340), .COUT(n1341), .S0(n108), .S1(n107));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302_add_4_19.INIT0 = 16'haaa0;
    defparam counter_296_302_add_4_19.INIT1 = 16'haaa0;
    defparam counter_296_302_add_4_19.INJECT1_0 = "NO";
    defparam counter_296_302_add_4_19.INJECT1_1 = "NO";
    LUT4 i2_3_lut_3_lut_4_lut_4_lut (.A(state[0]), .B(state[1]), .C(wants_to_write), 
         .D(i_ft_txe_n_c), .Z(n1360)) /* synthesis lut_function=(!(A+(B+((D)+!C)))) */ ;
    defparam i2_3_lut_3_lut_4_lut_4_lut.init = 16'h0010;
    BB io_ft_be_pad_0 (.I(VCC_net), .T(n1158), .B(io_ft_be[0]), .O(io_ft_be_out_0));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(60[9:17])
    OBZ io_ft_data_pad_15 (.I(GND_net), .T(n1158), .O(io_ft_data[15]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(57[9:19])
    OBZ io_ft_data_pad_14 (.I(GND_net), .T(n1158), .O(io_ft_data[14]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(57[9:19])
    PUR PUR_INST (.PUR(VCC_net));
    defparam PUR_INST.RST_PULSE = 1;
    OBZ io_ft_data_pad_13 (.I(GND_net), .T(n1158), .O(io_ft_data[13]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(57[9:19])
    CCU2C counter_296_302_add_4_25 (.A0(counter[23]), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(GND_net), .B1(GND_net), .C1(GND_net), .D1(GND_net), 
          .CIN(n1343), .S0(n102));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302_add_4_25.INIT0 = 16'haaa0;
    defparam counter_296_302_add_4_25.INIT1 = 16'h0000;
    defparam counter_296_302_add_4_25.INJECT1_0 = "NO";
    defparam counter_296_302_add_4_25.INJECT1_1 = "NO";
    OBZ io_ft_data_pad_12 (.I(GND_net), .T(n1158), .O(io_ft_data[12]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(57[9:19])
    OBZ io_ft_data_pad_11 (.I(GND_net), .T(n1158), .O(io_ft_data[11]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(57[9:19])
    OBZ io_ft_data_pad_10 (.I(GND_net), .T(n1158), .O(io_ft_data[10]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(57[9:19])
    OBZ io_ft_data_pad_9 (.I(GND_net), .T(n1158), .O(io_ft_data[9]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(57[9:19])
    OBZ io_ft_data_pad_8 (.I(GND_net), .T(n1158), .O(io_ft_data[8]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(57[9:19])
    OBZ io_ft_data_pad_7 (.I(ft_data_buf[7]), .T(n1158), .O(io_ft_data[7]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(57[9:19])
    OBZ io_ft_data_pad_6 (.I(VCC_net), .T(n1158), .O(io_ft_data[6]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(57[9:19])
    VLO i1 (.Z(GND_net));
    OBZ io_ft_data_pad_5 (.I(ft_data_buf[7]), .T(n1158), .O(io_ft_data[5]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(57[9:19])
    OBZ io_ft_data_pad_4 (.I(ft_data_buf[7]), .T(n1158), .O(io_ft_data[4]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(57[9:19])
    OBZ io_ft_data_pad_3 (.I(ft_data_buf[7]), .T(n1158), .O(io_ft_data[3]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(57[9:19])
    CCU2C counter_296_302_add_4_23 (.A0(n3), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n2), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n1342), .COUT(n1343), .S0(n104), .S1(n103));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302_add_4_23.INIT0 = 16'haaa0;
    defparam counter_296_302_add_4_23.INIT1 = 16'haaa0;
    defparam counter_296_302_add_4_23.INJECT1_0 = "NO";
    defparam counter_296_302_add_4_23.INJECT1_1 = "NO";
    OBZ io_ft_data_pad_2 (.I(ft_data_buf[7]), .T(n1158), .O(io_ft_data[2]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(57[9:19])
    OBZ io_ft_data_pad_1 (.I(VCC_net), .T(n1158), .O(io_ft_data[1]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(57[9:19])
    OBZ io_ft_data_pad_0 (.I(ft_data_buf[7]), .T(n1158), .O(io_ft_data[0]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(57[9:19])
    CCU2C counter_296_302_add_4_21 (.A0(n5), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n4), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n1341), .COUT(n1342), .S0(n106), .S1(n105));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[17:28])
    defparam counter_296_302_add_4_21.INIT0 = 16'haaa0;
    defparam counter_296_302_add_4_21.INIT1 = 16'haaa0;
    defparam counter_296_302_add_4_21.INJECT1_0 = "NO";
    defparam counter_296_302_add_4_21.INJECT1_1 = "NO";
    OB o_ft_wr_n_pad (.I(o_ft_wr_n_c), .O(o_ft_wr_n));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(12[21:30])
    OB o_ft_rd_n_pad (.I(o_ft_rd_n_c), .O(o_ft_rd_n));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(13[21:30])
    OB io_ft_oe_n_pad (.I(io_ft_oe_n_c), .O(io_ft_oe_n));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(14[21:31])
    OB o_leds_pad_7 (.I(o_leds_c_7), .O(o_leds[7]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(40[19:25])
    OB o_leds_pad_6 (.I(o_leds_c_6), .O(o_leds[6]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(40[19:25])
    OB o_leds_pad_5 (.I(o_leds_c_5), .O(o_leds[5]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(40[19:25])
    OB o_leds_pad_4 (.I(o_leds_c_4), .O(o_leds[4]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(40[19:25])
    OB o_leds_pad_3 (.I(o_leds_c_3), .O(o_leds[3]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(40[19:25])
    OB o_leds_pad_2 (.I(o_leds_c_2), .O(o_leds[2]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(40[19:25])
    OB o_leds_pad_1 (.I(o_leds_c_1), .O(o_leds[1]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(40[19:25])
    OB o_leds_pad_0 (.I(o_leds_c_0), .O(o_leds[0]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(40[19:25])
    IB i_clk16_pad (.I(i_clk16), .O(i_clk16_c));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(4[13:20])
    IB i_ft_clk_pad (.I(i_ft_clk), .O(i_ft_clk_c));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(8[21:29])
    IB i_ft_txe_n_pad (.I(i_ft_txe_n), .O(i_ft_txe_n_c));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(10[21:31])
    IB i_ft_rxf_n_pad (.I(i_ft_rxf_n), .O(i_ft_rxf_n_c));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(11[21:31])
    
endmodule
//
// Verilog Description of module PUR
// module not written out since it is a black-box. 
//

