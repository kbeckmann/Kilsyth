// Verilog netlist produced by program LSE :  version Diamond (64-bit) 3.10.3.144.3
// Netlist written on Wed Dec 19 00:44:18 2018
//
// Verilog Description of module kilsyth_top
//

module kilsyth_top (i_clk16, io_ft_data, i_ft_clk, i_ft_be, o_ft_txe_n, 
            o_ft_rxf_n, i_ft_wr_n, i_ft_rd_n, i_ft_oe_n, io_ft_gpio1, 
            o_leds) /* synthesis syn_module_defined=1 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(3[8:19])
    input i_clk16;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(4[13:20])
    input [15:0]io_ft_data;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(7[21:31])
    input i_ft_clk;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(8[21:29])
    input [1:0]i_ft_be;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(9[21:28])
    output o_ft_txe_n;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(10[21:31])
    output o_ft_rxf_n;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(11[21:31])
    input i_ft_wr_n;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(12[21:30])
    input i_ft_rd_n;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(13[21:30])
    input i_ft_oe_n;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(14[21:30])
    input io_ft_gpio1 /* synthesis .original_dir=IN_OUT */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(15[21:32])
    output [7:0]o_leds;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(40[19:25])
    
    wire GND_net /* synthesis RESET_NET_FOR_BUS20=20, DSPPORT_20=RST3 */ ;
    wire VCC_net /* synthesis CE_NET_FOR_BUS20=20, DSPPORT_20=CE3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(11[21:31])
    wire i_clk16_c /* synthesis DSPPORT_20=CLK3, CLOCK_NET_FOR_BUS20=20, is_clock=1, SET_AS_NETWORK=i_clk16_c */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(4[13:20])
    wire i_ft_clk_c /* synthesis is_clock=1, SET_AS_NETWORK=i_ft_clk_c */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(8[21:29])
    
    wire io_ft_data_c_15, io_ft_data_c_14, io_ft_data_c_13, io_ft_data_c_12, 
        io_ft_data_c_11, io_ft_data_c_10, io_ft_data_c_9, io_ft_data_c_8, 
        io_ft_data_c_7, io_ft_data_c_6, io_ft_data_c_5, io_ft_data_c_4, 
        io_ft_data_c_3, io_ft_data_c_2, io_ft_data_c_1, io_ft_data_c_0, 
        i_ft_be_c_1, i_ft_be_c_0, i_ft_wr_n_c, i_ft_rd_n_c, i_ft_oe_n_c, 
        io_ft_gpio1_c, o_leds_c_7, o_leds_c_6, o_leds_c_5, o_leds_c_4, 
        o_leds_c_3, o_leds_c_2, o_leds_c_1, o_leds_c_0, n24, n23;
    wire [25:0]counter;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(43[13:20])
    
    wire n22, n21, n20, n19, n18, n17, n16, n15, n14, n30, 
        n28, n26, n22_adj_1, n18_adj_2, n17_adj_3, n13, n12, n11, 
        n10, n9, n8, n7, n6, n5, n4, n3, n2, o_leds_7__N_1, 
        n102, n103, n104, n105, n106, n107, n108, n109, n110, 
        n111, n112, n113, n114, n115, n116, n117, n118, n119, 
        n120, n121, n122, n123, n124, n125, n186, n187, n188, 
        n189, n190, n191, n192, n193, n194, n195, n196, n197;
    
    VHI i2 (.Z(VCC_net));
    FD1S3AX leds_5__17 (.D(i_ft_oe_n_c), .CK(i_clk16_c), .Q(o_leds_c_5)) /* synthesis lse_init_val=0 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(53[9] 61[5])
    defparam leds_5__17.GSR = "ENABLED";
    FD1S3AX leds_4__18 (.D(i_ft_rd_n_c), .CK(i_clk16_c), .Q(o_leds_c_4)) /* synthesis lse_init_val=0 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(53[9] 61[5])
    defparam leds_4__18.GSR = "ENABLED";
    FD1S3AX leds_3__19 (.D(i_ft_wr_n_c), .CK(i_clk16_c), .Q(o_leds_c_3)) /* synthesis lse_init_val=0 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(53[9] 61[5])
    defparam leds_3__19.GSR = "ENABLED";
    FD1S3AX leds_2__20 (.D(i_ft_be_c_1), .CK(i_clk16_c), .Q(o_leds_c_2)) /* synthesis lse_init_val=0 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(53[9] 61[5])
    defparam leds_2__20.GSR = "ENABLED";
    FD1S3AX leds_1__21 (.D(i_ft_be_c_0), .CK(i_clk16_c), .Q(o_leds_c_1)) /* synthesis lse_init_val=0 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(53[9] 61[5])
    defparam leds_1__21.GSR = "ENABLED";
    FD1S3AX leds_0__22 (.D(counter[23]), .CK(i_clk16_c), .Q(o_leds_c_0)) /* synthesis lse_init_val=0 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(53[9] 61[5])
    defparam leds_0__22.GSR = "ENABLED";
    FD1S3AX leds_7__23 (.D(o_leds_7__N_1), .CK(i_ft_clk_c), .Q(o_leds_c_7)) /* synthesis lse_init_val=0 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(64[9] 66[5])
    defparam leds_7__23.GSR = "ENABLED";
    FD1S3AX counter_26_27__i23 (.D(n102), .CK(i_clk16_c), .Q(counter[23])) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27__i23.GSR = "ENABLED";
    OB o_ft_txe_n_pad (.I(VCC_net), .O(o_ft_txe_n));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(10[21:31])
    LUT4 i10_4_lut (.A(io_ft_data_c_9), .B(io_ft_data_c_3), .C(io_ft_data_c_2), 
         .D(io_ft_data_c_1), .Z(n26)) /* synthesis lut_function=(A+(B+(C+(D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(65[14:25])
    defparam i10_4_lut.init = 16'hfffe;
    OB o_ft_rxf_n_pad (.I(VCC_net), .O(o_ft_rxf_n));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(11[21:31])
    GSR GSR_INST (.GSR(VCC_net));
    LUT4 i14_4_lut (.A(io_ft_data_c_15), .B(n28), .C(n22_adj_1), .D(io_ft_data_c_14), 
         .Z(n30)) /* synthesis lut_function=(A+(B+(C+(D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(65[14:25])
    defparam i14_4_lut.init = 16'hfffe;
    LUT4 i12_4_lut (.A(io_ft_data_c_5), .B(io_ft_data_c_4), .C(io_ft_data_c_13), 
         .D(io_ft_data_c_6), .Z(n28)) /* synthesis lut_function=(A+(B+(C+(D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(65[14:25])
    defparam i12_4_lut.init = 16'hfffe;
    LUT4 i1_2_lut (.A(io_ft_data_c_0), .B(io_ft_data_c_10), .Z(n17_adj_3)) /* synthesis lut_function=(A+(B)) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(65[14:25])
    defparam i1_2_lut.init = 16'heeee;
    LUT4 i15_4_lut (.A(n17_adj_3), .B(n30), .C(n26), .D(n18_adj_2), 
         .Z(o_leds_7__N_1)) /* synthesis lut_function=(A+(B+(C+(D)))) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(65[14:25])
    defparam i15_4_lut.init = 16'hfffe;
    LUT4 i2_2_lut (.A(io_ft_data_c_11), .B(io_ft_data_c_8), .Z(n18_adj_2)) /* synthesis lut_function=(A+(B)) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(65[14:25])
    defparam i2_2_lut.init = 16'heeee;
    PUR PUR_INST (.PUR(VCC_net));
    defparam PUR_INST.RST_PULSE = 1;
    LUT4 i6_2_lut (.A(io_ft_data_c_7), .B(io_ft_data_c_12), .Z(n22_adj_1)) /* synthesis lut_function=(A+(B)) */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(65[14:25])
    defparam i6_2_lut.init = 16'heeee;
    VLO i1 (.Z(GND_net));
    CCU2C counter_26_27_add_4_25 (.A0(counter[23]), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(GND_net), .B1(GND_net), .C1(GND_net), .D1(GND_net), 
          .CIN(n197), .S0(n102));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27_add_4_25.INIT0 = 16'haaa0;
    defparam counter_26_27_add_4_25.INIT1 = 16'h0000;
    defparam counter_26_27_add_4_25.INJECT1_0 = "NO";
    defparam counter_26_27_add_4_25.INJECT1_1 = "NO";
    CCU2C counter_26_27_add_4_23 (.A0(n3), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n2), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n196), .COUT(n197), .S0(n104), .S1(n103));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27_add_4_23.INIT0 = 16'haaa0;
    defparam counter_26_27_add_4_23.INIT1 = 16'haaa0;
    defparam counter_26_27_add_4_23.INJECT1_0 = "NO";
    defparam counter_26_27_add_4_23.INJECT1_1 = "NO";
    CCU2C counter_26_27_add_4_21 (.A0(n5), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n4), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n195), .COUT(n196), .S0(n106), .S1(n105));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27_add_4_21.INIT0 = 16'haaa0;
    defparam counter_26_27_add_4_21.INIT1 = 16'haaa0;
    defparam counter_26_27_add_4_21.INJECT1_0 = "NO";
    defparam counter_26_27_add_4_21.INJECT1_1 = "NO";
    CCU2C counter_26_27_add_4_19 (.A0(n7), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n6), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n194), .COUT(n195), .S0(n108), .S1(n107));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27_add_4_19.INIT0 = 16'haaa0;
    defparam counter_26_27_add_4_19.INIT1 = 16'haaa0;
    defparam counter_26_27_add_4_19.INJECT1_0 = "NO";
    defparam counter_26_27_add_4_19.INJECT1_1 = "NO";
    CCU2C counter_26_27_add_4_17 (.A0(n9), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n8), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n193), .COUT(n194), .S0(n110), .S1(n109));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27_add_4_17.INIT0 = 16'haaa0;
    defparam counter_26_27_add_4_17.INIT1 = 16'haaa0;
    defparam counter_26_27_add_4_17.INJECT1_0 = "NO";
    defparam counter_26_27_add_4_17.INJECT1_1 = "NO";
    CCU2C counter_26_27_add_4_15 (.A0(n11), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n10), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n192), .COUT(n193), .S0(n112), .S1(n111));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27_add_4_15.INIT0 = 16'haaa0;
    defparam counter_26_27_add_4_15.INIT1 = 16'haaa0;
    defparam counter_26_27_add_4_15.INJECT1_0 = "NO";
    defparam counter_26_27_add_4_15.INJECT1_1 = "NO";
    CCU2C counter_26_27_add_4_13 (.A0(n13), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n12), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n191), .COUT(n192), .S0(n114), .S1(n113));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27_add_4_13.INIT0 = 16'haaa0;
    defparam counter_26_27_add_4_13.INIT1 = 16'haaa0;
    defparam counter_26_27_add_4_13.INJECT1_0 = "NO";
    defparam counter_26_27_add_4_13.INJECT1_1 = "NO";
    CCU2C counter_26_27_add_4_11 (.A0(n15), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n14), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n190), .COUT(n191), .S0(n116), .S1(n115));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27_add_4_11.INIT0 = 16'haaa0;
    defparam counter_26_27_add_4_11.INIT1 = 16'haaa0;
    defparam counter_26_27_add_4_11.INJECT1_0 = "NO";
    defparam counter_26_27_add_4_11.INJECT1_1 = "NO";
    CCU2C counter_26_27_add_4_9 (.A0(n17), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n16), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n189), .COUT(n190), .S0(n118), .S1(n117));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27_add_4_9.INIT0 = 16'haaa0;
    defparam counter_26_27_add_4_9.INIT1 = 16'haaa0;
    defparam counter_26_27_add_4_9.INJECT1_0 = "NO";
    defparam counter_26_27_add_4_9.INJECT1_1 = "NO";
    CCU2C counter_26_27_add_4_7 (.A0(n19), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n18), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n188), .COUT(n189), .S0(n120), .S1(n119));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27_add_4_7.INIT0 = 16'haaa0;
    defparam counter_26_27_add_4_7.INIT1 = 16'haaa0;
    defparam counter_26_27_add_4_7.INJECT1_0 = "NO";
    defparam counter_26_27_add_4_7.INJECT1_1 = "NO";
    CCU2C counter_26_27_add_4_5 (.A0(n21), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n20), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n187), .COUT(n188), .S0(n122), .S1(n121));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27_add_4_5.INIT0 = 16'haaa0;
    defparam counter_26_27_add_4_5.INIT1 = 16'haaa0;
    defparam counter_26_27_add_4_5.INJECT1_0 = "NO";
    defparam counter_26_27_add_4_5.INJECT1_1 = "NO";
    CCU2C counter_26_27_add_4_3 (.A0(n23), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(n22), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n186), .COUT(n187), .S0(n124), .S1(n123));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27_add_4_3.INIT0 = 16'haaa0;
    defparam counter_26_27_add_4_3.INIT1 = 16'haaa0;
    defparam counter_26_27_add_4_3.INJECT1_0 = "NO";
    defparam counter_26_27_add_4_3.INJECT1_1 = "NO";
    FD1S3AX leds_6__16 (.D(io_ft_gpio1_c), .CK(i_clk16_c), .Q(o_leds_c_6)) /* synthesis lse_init_val=0 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(53[9] 61[5])
    defparam leds_6__16.GSR = "ENABLED";
    FD1S3AX counter_26_27__i22 (.D(n103), .CK(i_clk16_c), .Q(n2)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27__i22.GSR = "ENABLED";
    FD1S3AX counter_26_27__i21 (.D(n104), .CK(i_clk16_c), .Q(n3)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27__i21.GSR = "ENABLED";
    FD1S3AX counter_26_27__i20 (.D(n105), .CK(i_clk16_c), .Q(n4)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27__i20.GSR = "ENABLED";
    FD1S3AX counter_26_27__i19 (.D(n106), .CK(i_clk16_c), .Q(n5)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27__i19.GSR = "ENABLED";
    FD1S3AX counter_26_27__i18 (.D(n107), .CK(i_clk16_c), .Q(n6)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27__i18.GSR = "ENABLED";
    FD1S3AX counter_26_27__i17 (.D(n108), .CK(i_clk16_c), .Q(n7)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27__i17.GSR = "ENABLED";
    FD1S3AX counter_26_27__i16 (.D(n109), .CK(i_clk16_c), .Q(n8)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27__i16.GSR = "ENABLED";
    FD1S3AX counter_26_27__i15 (.D(n110), .CK(i_clk16_c), .Q(n9)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27__i15.GSR = "ENABLED";
    FD1S3AX counter_26_27__i14 (.D(n111), .CK(i_clk16_c), .Q(n10)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27__i14.GSR = "ENABLED";
    FD1S3AX counter_26_27__i13 (.D(n112), .CK(i_clk16_c), .Q(n11)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27__i13.GSR = "ENABLED";
    FD1S3AX counter_26_27__i12 (.D(n113), .CK(i_clk16_c), .Q(n12)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27__i12.GSR = "ENABLED";
    FD1S3AX counter_26_27__i11 (.D(n114), .CK(i_clk16_c), .Q(n13)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27__i11.GSR = "ENABLED";
    FD1S3AX counter_26_27__i10 (.D(n115), .CK(i_clk16_c), .Q(n14)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27__i10.GSR = "ENABLED";
    FD1S3AX counter_26_27__i9 (.D(n116), .CK(i_clk16_c), .Q(n15)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27__i9.GSR = "ENABLED";
    FD1S3AX counter_26_27__i8 (.D(n117), .CK(i_clk16_c), .Q(n16)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27__i8.GSR = "ENABLED";
    FD1S3AX counter_26_27__i7 (.D(n118), .CK(i_clk16_c), .Q(n17)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27__i7.GSR = "ENABLED";
    FD1S3AX counter_26_27__i6 (.D(n119), .CK(i_clk16_c), .Q(n18)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27__i6.GSR = "ENABLED";
    FD1S3AX counter_26_27__i5 (.D(n120), .CK(i_clk16_c), .Q(n19)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27__i5.GSR = "ENABLED";
    FD1S3AX counter_26_27__i4 (.D(n121), .CK(i_clk16_c), .Q(n20)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27__i4.GSR = "ENABLED";
    FD1S3AX counter_26_27__i3 (.D(n122), .CK(i_clk16_c), .Q(n21)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27__i3.GSR = "ENABLED";
    FD1S3AX counter_26_27__i2 (.D(n123), .CK(i_clk16_c), .Q(n22)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27__i2.GSR = "ENABLED";
    FD1S3AX counter_26_27__i1 (.D(n124), .CK(i_clk16_c), .Q(n23)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27__i1.GSR = "ENABLED";
    FD1S3AX counter_26_27__i0 (.D(n125), .CK(i_clk16_c), .Q(n24)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27__i0.GSR = "ENABLED";
    CCU2C counter_26_27_add_4_1 (.A0(GND_net), .B0(GND_net), .C0(GND_net), 
          .D0(GND_net), .A1(n24), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .COUT(n186), .S1(n125));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(54[17:28])
    defparam counter_26_27_add_4_1.INIT0 = 16'h0000;
    defparam counter_26_27_add_4_1.INIT1 = 16'h555f;
    defparam counter_26_27_add_4_1.INJECT1_0 = "NO";
    defparam counter_26_27_add_4_1.INJECT1_1 = "NO";
    OB o_leds_pad_7 (.I(o_leds_c_7), .O(o_leds[7]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(40[19:25])
    OB o_leds_pad_6 (.I(o_leds_c_6), .O(o_leds[6]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(40[19:25])
    OB o_leds_pad_5 (.I(o_leds_c_5), .O(o_leds[5]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(40[19:25])
    OB o_leds_pad_4 (.I(o_leds_c_4), .O(o_leds[4]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(40[19:25])
    OB o_leds_pad_3 (.I(o_leds_c_3), .O(o_leds[3]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(40[19:25])
    OB o_leds_pad_2 (.I(o_leds_c_2), .O(o_leds[2]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(40[19:25])
    OB o_leds_pad_1 (.I(o_leds_c_1), .O(o_leds[1]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(40[19:25])
    OB o_leds_pad_0 (.I(o_leds_c_0), .O(o_leds[0]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(40[19:25])
    IB i_clk16_pad (.I(i_clk16), .O(i_clk16_c));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(4[13:20])
    IB io_ft_data_pad_15 (.I(io_ft_data[15]), .O(io_ft_data_c_15));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(7[21:31])
    IB io_ft_data_pad_14 (.I(io_ft_data[14]), .O(io_ft_data_c_14));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(7[21:31])
    IB io_ft_data_pad_13 (.I(io_ft_data[13]), .O(io_ft_data_c_13));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(7[21:31])
    IB io_ft_data_pad_12 (.I(io_ft_data[12]), .O(io_ft_data_c_12));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(7[21:31])
    IB io_ft_data_pad_11 (.I(io_ft_data[11]), .O(io_ft_data_c_11));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(7[21:31])
    IB io_ft_data_pad_10 (.I(io_ft_data[10]), .O(io_ft_data_c_10));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(7[21:31])
    IB io_ft_data_pad_9 (.I(io_ft_data[9]), .O(io_ft_data_c_9));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(7[21:31])
    IB io_ft_data_pad_8 (.I(io_ft_data[8]), .O(io_ft_data_c_8));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(7[21:31])
    IB io_ft_data_pad_7 (.I(io_ft_data[7]), .O(io_ft_data_c_7));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(7[21:31])
    IB io_ft_data_pad_6 (.I(io_ft_data[6]), .O(io_ft_data_c_6));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(7[21:31])
    IB io_ft_data_pad_5 (.I(io_ft_data[5]), .O(io_ft_data_c_5));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(7[21:31])
    IB io_ft_data_pad_4 (.I(io_ft_data[4]), .O(io_ft_data_c_4));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(7[21:31])
    IB io_ft_data_pad_3 (.I(io_ft_data[3]), .O(io_ft_data_c_3));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(7[21:31])
    IB io_ft_data_pad_2 (.I(io_ft_data[2]), .O(io_ft_data_c_2));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(7[21:31])
    IB io_ft_data_pad_1 (.I(io_ft_data[1]), .O(io_ft_data_c_1));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(7[21:31])
    IB io_ft_data_pad_0 (.I(io_ft_data[0]), .O(io_ft_data_c_0));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(7[21:31])
    IB i_ft_clk_pad (.I(i_ft_clk), .O(i_ft_clk_c));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(8[21:29])
    IB i_ft_be_pad_1 (.I(i_ft_be[1]), .O(i_ft_be_c_1));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(9[21:28])
    IB i_ft_be_pad_0 (.I(i_ft_be[0]), .O(i_ft_be_c_0));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(9[21:28])
    IB i_ft_wr_n_pad (.I(i_ft_wr_n), .O(i_ft_wr_n_c));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(12[21:30])
    IB i_ft_rd_n_pad (.I(i_ft_rd_n), .O(i_ft_rd_n_c));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(13[21:30])
    IB i_ft_oe_n_pad (.I(i_ft_oe_n), .O(i_ft_oe_n_c));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(14[21:30])
    IB io_ft_gpio1_pad (.I(io_ft_gpio1), .O(io_ft_gpio1_c));   // /home/konrad/dev/Kilsyth/gateware/bootloader/src/kilsyth_top.v(15[21:32])
    
endmodule
//
// Verilog Description of module PUR
// module not written out since it is a black-box. 
//

