// Verilog netlist produced by program LSE :  version Diamond (64-bit) 3.10.3.144.3
// Netlist written on Tue Dec 11 21:19:35 2018
//
// Verilog Description of module top
//

module top (clk, leds) /* synthesis syn_module_defined=1 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(3[8:11])
    input clk;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(3[23:26])
    output [7:0]leds;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(3[46:50])
    
    wire GND_net /* synthesis RESET_NET_FOR_BUS20=20, DSPPORT_20=RST3 */ ;
    wire VCC_net /* synthesis CE_NET_FOR_BUS20=20, DSPPORT_20=CE3 */ ;
    wire clk_c /* synthesis DSPPORT_20=CLK3, CLOCK_NET_FOR_BUS20=20, is_clock=1, SET_AS_NETWORK=clk_c */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(3[23:26])
    
    wire leds_c_7, leds_c_6, leds_c_5, leds_c_4, leds_c_3, leds_c_2, 
        leds_c_1, leds_c_0, n26, n25, n24, n23, n22, n21, n20, 
        n19, n18, n17, n16, n15, n14, n13, n12, n11, n10, 
        n9, n110, n111, n112, n113, n114, n115, n116, n117, 
        n118, n119, n120, n121, n122, n123, n124, n125, n126, 
        n127, n128, n129, n130, n131, n132, n133, n134, n135, 
        n156, n157, n158, n159, n160, n161, n162, n163, n164, 
        n165, n166, n167, n168;
    
    VHI i2 (.Z(VCC_net));
    OB leds_pad_7 (.I(leds_c_7), .O(leds[7]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(3[46:50])
    VLO i1 (.Z(GND_net));
    OB leds_pad_6 (.I(leds_c_6), .O(leds[6]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(3[46:50])
    GSR GSR_INST (.GSR(VCC_net));
    PUR PUR_INST (.PUR(VCC_net));
    defparam PUR_INST.RST_PULSE = 1;
    CCU2C counter_9_add_4_27 (.A0(leds_c_7), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(GND_net), .B1(GND_net), .C1(GND_net), .D1(GND_net), 
          .CIN(n168), .S0(n110));   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9_add_4_27.INIT0 = 16'haaa0;
    defparam counter_9_add_4_27.INIT1 = 16'h0000;
    defparam counter_9_add_4_27.INJECT1_0 = "NO";
    defparam counter_9_add_4_27.INJECT1_1 = "NO";
    CCU2C counter_9_add_4_25 (.A0(leds_c_5), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(leds_c_6), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n167), .COUT(n168), .S0(n112), .S1(n111));   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9_add_4_25.INIT0 = 16'haaa0;
    defparam counter_9_add_4_25.INIT1 = 16'haaa0;
    defparam counter_9_add_4_25.INJECT1_0 = "NO";
    defparam counter_9_add_4_25.INJECT1_1 = "NO";
    CCU2C counter_9_add_4_23 (.A0(leds_c_3), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(leds_c_4), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n166), .COUT(n167), .S0(n114), .S1(n113));   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9_add_4_23.INIT0 = 16'haaa0;
    defparam counter_9_add_4_23.INIT1 = 16'haaa0;
    defparam counter_9_add_4_23.INJECT1_0 = "NO";
    defparam counter_9_add_4_23.INJECT1_1 = "NO";
    CCU2C counter_9_add_4_21 (.A0(leds_c_1), .B0(GND_net), .C0(GND_net), 
          .D0(VCC_net), .A1(leds_c_2), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .CIN(n165), .COUT(n166), .S0(n116), .S1(n115));   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9_add_4_21.INIT0 = 16'haaa0;
    defparam counter_9_add_4_21.INIT1 = 16'haaa0;
    defparam counter_9_add_4_21.INJECT1_0 = "NO";
    defparam counter_9_add_4_21.INJECT1_1 = "NO";
    CCU2C counter_9_add_4_19 (.A0(n9), .B0(GND_net), .C0(GND_net), .D0(VCC_net), 
          .A1(leds_c_0), .B1(GND_net), .C1(GND_net), .D1(VCC_net), .CIN(n164), 
          .COUT(n165), .S0(n118), .S1(n117));   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9_add_4_19.INIT0 = 16'haaa0;
    defparam counter_9_add_4_19.INIT1 = 16'haaa0;
    defparam counter_9_add_4_19.INJECT1_0 = "NO";
    defparam counter_9_add_4_19.INJECT1_1 = "NO";
    CCU2C counter_9_add_4_17 (.A0(n11), .B0(GND_net), .C0(GND_net), .D0(VCC_net), 
          .A1(n10), .B1(GND_net), .C1(GND_net), .D1(VCC_net), .CIN(n163), 
          .COUT(n164), .S0(n120), .S1(n119));   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9_add_4_17.INIT0 = 16'haaa0;
    defparam counter_9_add_4_17.INIT1 = 16'haaa0;
    defparam counter_9_add_4_17.INJECT1_0 = "NO";
    defparam counter_9_add_4_17.INJECT1_1 = "NO";
    CCU2C counter_9_add_4_15 (.A0(n13), .B0(GND_net), .C0(GND_net), .D0(VCC_net), 
          .A1(n12), .B1(GND_net), .C1(GND_net), .D1(VCC_net), .CIN(n162), 
          .COUT(n163), .S0(n122), .S1(n121));   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9_add_4_15.INIT0 = 16'haaa0;
    defparam counter_9_add_4_15.INIT1 = 16'haaa0;
    defparam counter_9_add_4_15.INJECT1_0 = "NO";
    defparam counter_9_add_4_15.INJECT1_1 = "NO";
    CCU2C counter_9_add_4_13 (.A0(n15), .B0(GND_net), .C0(GND_net), .D0(VCC_net), 
          .A1(n14), .B1(GND_net), .C1(GND_net), .D1(VCC_net), .CIN(n161), 
          .COUT(n162), .S0(n124), .S1(n123));   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9_add_4_13.INIT0 = 16'haaa0;
    defparam counter_9_add_4_13.INIT1 = 16'haaa0;
    defparam counter_9_add_4_13.INJECT1_0 = "NO";
    defparam counter_9_add_4_13.INJECT1_1 = "NO";
    CCU2C counter_9_add_4_11 (.A0(n17), .B0(GND_net), .C0(GND_net), .D0(VCC_net), 
          .A1(n16), .B1(GND_net), .C1(GND_net), .D1(VCC_net), .CIN(n160), 
          .COUT(n161), .S0(n126), .S1(n125));   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9_add_4_11.INIT0 = 16'haaa0;
    defparam counter_9_add_4_11.INIT1 = 16'haaa0;
    defparam counter_9_add_4_11.INJECT1_0 = "NO";
    defparam counter_9_add_4_11.INJECT1_1 = "NO";
    CCU2C counter_9_add_4_9 (.A0(n19), .B0(GND_net), .C0(GND_net), .D0(VCC_net), 
          .A1(n18), .B1(GND_net), .C1(GND_net), .D1(VCC_net), .CIN(n159), 
          .COUT(n160), .S0(n128), .S1(n127));   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9_add_4_9.INIT0 = 16'haaa0;
    defparam counter_9_add_4_9.INIT1 = 16'haaa0;
    defparam counter_9_add_4_9.INJECT1_0 = "NO";
    defparam counter_9_add_4_9.INJECT1_1 = "NO";
    CCU2C counter_9_add_4_7 (.A0(n21), .B0(GND_net), .C0(GND_net), .D0(VCC_net), 
          .A1(n20), .B1(GND_net), .C1(GND_net), .D1(VCC_net), .CIN(n158), 
          .COUT(n159), .S0(n130), .S1(n129));   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9_add_4_7.INIT0 = 16'haaa0;
    defparam counter_9_add_4_7.INIT1 = 16'haaa0;
    defparam counter_9_add_4_7.INJECT1_0 = "NO";
    defparam counter_9_add_4_7.INJECT1_1 = "NO";
    CCU2C counter_9_add_4_5 (.A0(n23), .B0(GND_net), .C0(GND_net), .D0(VCC_net), 
          .A1(n22), .B1(GND_net), .C1(GND_net), .D1(VCC_net), .CIN(n157), 
          .COUT(n158), .S0(n132), .S1(n131));   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9_add_4_5.INIT0 = 16'haaa0;
    defparam counter_9_add_4_5.INIT1 = 16'haaa0;
    defparam counter_9_add_4_5.INJECT1_0 = "NO";
    defparam counter_9_add_4_5.INJECT1_1 = "NO";
    CCU2C counter_9_add_4_3 (.A0(n25), .B0(GND_net), .C0(GND_net), .D0(VCC_net), 
          .A1(n24), .B1(GND_net), .C1(GND_net), .D1(VCC_net), .CIN(n156), 
          .COUT(n157), .S0(n134), .S1(n133));   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9_add_4_3.INIT0 = 16'haaa0;
    defparam counter_9_add_4_3.INIT1 = 16'haaa0;
    defparam counter_9_add_4_3.INJECT1_0 = "NO";
    defparam counter_9_add_4_3.INJECT1_1 = "NO";
    FD1S3AX counter_9__i25 (.D(n110), .CK(clk_c), .Q(leds_c_7)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i25.GSR = "ENABLED";
    FD1S3AX counter_9__i24 (.D(n111), .CK(clk_c), .Q(leds_c_6)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i24.GSR = "ENABLED";
    FD1S3AX counter_9__i23 (.D(n112), .CK(clk_c), .Q(leds_c_5)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i23.GSR = "ENABLED";
    FD1S3AX counter_9__i22 (.D(n113), .CK(clk_c), .Q(leds_c_4)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i22.GSR = "ENABLED";
    FD1S3AX counter_9__i21 (.D(n114), .CK(clk_c), .Q(leds_c_3)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i21.GSR = "ENABLED";
    FD1S3AX counter_9__i20 (.D(n115), .CK(clk_c), .Q(leds_c_2)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i20.GSR = "ENABLED";
    FD1S3AX counter_9__i19 (.D(n116), .CK(clk_c), .Q(leds_c_1)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i19.GSR = "ENABLED";
    FD1S3AX counter_9__i18 (.D(n117), .CK(clk_c), .Q(leds_c_0)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i18.GSR = "ENABLED";
    FD1S3AX counter_9__i17 (.D(n118), .CK(clk_c), .Q(n9)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i17.GSR = "ENABLED";
    FD1S3AX counter_9__i16 (.D(n119), .CK(clk_c), .Q(n10)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i16.GSR = "ENABLED";
    FD1S3AX counter_9__i15 (.D(n120), .CK(clk_c), .Q(n11)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i15.GSR = "ENABLED";
    FD1S3AX counter_9__i14 (.D(n121), .CK(clk_c), .Q(n12)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i14.GSR = "ENABLED";
    FD1S3AX counter_9__i13 (.D(n122), .CK(clk_c), .Q(n13)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i13.GSR = "ENABLED";
    FD1S3AX counter_9__i12 (.D(n123), .CK(clk_c), .Q(n14)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i12.GSR = "ENABLED";
    FD1S3AX counter_9__i11 (.D(n124), .CK(clk_c), .Q(n15)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i11.GSR = "ENABLED";
    FD1S3AX counter_9__i10 (.D(n125), .CK(clk_c), .Q(n16)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i10.GSR = "ENABLED";
    FD1S3AX counter_9__i9 (.D(n126), .CK(clk_c), .Q(n17)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i9.GSR = "ENABLED";
    FD1S3AX counter_9__i8 (.D(n127), .CK(clk_c), .Q(n18)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i8.GSR = "ENABLED";
    FD1S3AX counter_9__i7 (.D(n128), .CK(clk_c), .Q(n19)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i7.GSR = "ENABLED";
    FD1S3AX counter_9__i6 (.D(n129), .CK(clk_c), .Q(n20)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i6.GSR = "ENABLED";
    FD1S3AX counter_9__i5 (.D(n130), .CK(clk_c), .Q(n21)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i5.GSR = "ENABLED";
    FD1S3AX counter_9__i4 (.D(n131), .CK(clk_c), .Q(n22)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i4.GSR = "ENABLED";
    FD1S3AX counter_9__i3 (.D(n132), .CK(clk_c), .Q(n23)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i3.GSR = "ENABLED";
    FD1S3AX counter_9__i2 (.D(n133), .CK(clk_c), .Q(n24)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i2.GSR = "ENABLED";
    FD1S3AX counter_9__i1 (.D(n134), .CK(clk_c), .Q(n25)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i1.GSR = "ENABLED";
    FD1S3AX counter_9__i0 (.D(n135), .CK(clk_c), .Q(n26)) /* synthesis syn_use_carry_chain=1, REG_OUTPUT_CLK=CLK3, REG_OUTPUT_CE=CE3, REG_OUTPUT_RST=RST3 */ ;   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9__i0.GSR = "ENABLED";
    CCU2C counter_9_add_4_1 (.A0(GND_net), .B0(GND_net), .C0(GND_net), 
          .D0(GND_net), .A1(n26), .B1(GND_net), .C1(GND_net), .D1(VCC_net), 
          .COUT(n156), .S1(n135));   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(8[14:25])
    defparam counter_9_add_4_1.INIT0 = 16'h0000;
    defparam counter_9_add_4_1.INIT1 = 16'h555f;
    defparam counter_9_add_4_1.INJECT1_0 = "NO";
    defparam counter_9_add_4_1.INJECT1_1 = "NO";
    OB leds_pad_5 (.I(leds_c_5), .O(leds[5]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(3[46:50])
    OB leds_pad_4 (.I(leds_c_4), .O(leds[4]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(3[46:50])
    OB leds_pad_3 (.I(leds_c_3), .O(leds[3]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(3[46:50])
    OB leds_pad_2 (.I(leds_c_2), .O(leds[2]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(3[46:50])
    OB leds_pad_1 (.I(leds_c_1), .O(leds[1]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(3[46:50])
    OB leds_pad_0 (.I(leds_c_0), .O(leds[0]));   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(3[46:50])
    IB clk_pad (.I(clk), .O(clk_c));   // /home/konrad/dev/Kilsyth/gateware/bootloader/top.v(3[23:26])
    
endmodule
//
// Verilog Description of module PUR
// module not written out since it is a black-box. 
//

