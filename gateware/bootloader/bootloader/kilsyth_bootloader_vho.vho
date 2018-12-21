
-- VHDL netlist produced by program ldbanno, Version Diamond (64-bit) 3.10.3.144.3

-- ldbanno -n VHDL -o kilsyth_bootloader_vho.vho -w -neg -gui -msgset /home/konrad/dev/Kilsyth/gateware/bootloader/promote.xml kilsyth_bootloader.ncd 
-- Netlist created on Fri Dec 21 00:08:13 2018
-- Netlist written on Fri Dec 21 00:08:28 2018
-- Design is for device LFE5U-12F
-- Design is for package CABGA381
-- Design is for performance grade 6

-- entity sapiobuf
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity sapiobuf is
    port (I: in Std_logic; T: in Std_logic; PAD: out Std_logic);

    ATTRIBUTE Vital_Level0 OF sapiobuf : ENTITY IS TRUE;

  end sapiobuf;

  architecture Structure of sapiobuf is
  begin
    INST5: OBZ
      port map (I=>I, T=>T, O=>PAD);
  end Structure;

-- entity gnd
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity gnd is
    port (PWR0: out Std_logic);

    ATTRIBUTE Vital_Level0 OF gnd : ENTITY IS TRUE;

  end gnd;

  architecture Structure of gnd is
  begin
    INST1: VLO
      port map (Z=>PWR0);
  end Structure;

-- entity inverter
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity inverter is
    port (I: in Std_logic; Z: out Std_logic);

    ATTRIBUTE Vital_Level0 OF inverter : ENTITY IS TRUE;

  end inverter;

  architecture Structure of inverter is
  begin
    INST1: INV
      port map (A=>I, Z=>Z);
  end Structure;

-- entity io_ft_data_15_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity io_ft_data_15_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "io_ft_data_15_B";

      tipd_PADDT  	: VitalDelayType01 := (0 ns, 0 ns);

        tpd_PADDT_ioftdata15	 : VitalDelayType01Z := (0 ns, 0 ns, 0 ns , 0 ns, 0 ns, 0 ns)
        );

    port (PADDT: in Std_logic; ioftdata15: out Std_logic);

    ATTRIBUTE Vital_Level0 OF io_ft_data_15_B : ENTITY IS TRUE;

  end io_ft_data_15_B;

  architecture Structure of io_ft_data_15_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDT_ipd 	: std_logic := 'X';
    signal ioftdata15_out 	: std_logic := 'X';

    signal GNDI: Std_logic;
    signal PADDT_NOTIN: Std_logic;
    component sapiobuf
      port (I: in Std_logic; T: in Std_logic; PAD: out Std_logic);
    end component;
    component gnd
      port (PWR0: out Std_logic);
    end component;
    component inverter
      port (I: in Std_logic; Z: out Std_logic);
    end component;
  begin
    io_ft_data_pad_15: sapiobuf
      port map (I=>GNDI, T=>PADDT_NOTIN, PAD=>ioftdata15_out);
    DRIVEGND: gnd
      port map (PWR0=>GNDI);
    PADDT_INVERTERIN: inverter
      port map (I=>PADDT_ipd, Z=>PADDT_NOTIN);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDT_ipd, PADDT, tipd_PADDT);
    END BLOCK;

    VitalBehavior : PROCESS (PADDT_ipd, ioftdata15_out)
    VARIABLE ioftdata15_zd         	: std_logic := 'X';
    VARIABLE ioftdata15_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    ioftdata15_zd 	:= ioftdata15_out;

    VitalPathDelay01Z (

        OutSignal => ioftdata15, OutSignalName => "ioftdata15", OutTemp => ioftdata15_zd,
      Paths      => (0 => (InputChangeTime => PADDT_ipd'last_event,
                           PathDelay => tpd_PADDT_ioftdata15,
                           PathCondition => TRUE)),
      GlitchData => ioftdata15_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity io_ft_data_14_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity io_ft_data_14_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "io_ft_data_14_B";

      tipd_PADDT  	: VitalDelayType01 := (0 ns, 0 ns);

        tpd_PADDT_ioftdata14	 : VitalDelayType01Z := (0 ns, 0 ns, 0 ns , 0 ns, 0 ns, 0 ns)
        );

    port (PADDT: in Std_logic; ioftdata14: out Std_logic);

    ATTRIBUTE Vital_Level0 OF io_ft_data_14_B : ENTITY IS TRUE;

  end io_ft_data_14_B;

  architecture Structure of io_ft_data_14_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDT_ipd 	: std_logic := 'X';
    signal ioftdata14_out 	: std_logic := 'X';

    signal GNDI: Std_logic;
    signal PADDT_NOTIN: Std_logic;
    component sapiobuf
      port (I: in Std_logic; T: in Std_logic; PAD: out Std_logic);
    end component;
    component gnd
      port (PWR0: out Std_logic);
    end component;
    component inverter
      port (I: in Std_logic; Z: out Std_logic);
    end component;
  begin
    io_ft_data_pad_14: sapiobuf
      port map (I=>GNDI, T=>PADDT_NOTIN, PAD=>ioftdata14_out);
    DRIVEGND: gnd
      port map (PWR0=>GNDI);
    PADDT_INVERTERIN: inverter
      port map (I=>PADDT_ipd, Z=>PADDT_NOTIN);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDT_ipd, PADDT, tipd_PADDT);
    END BLOCK;

    VitalBehavior : PROCESS (PADDT_ipd, ioftdata14_out)
    VARIABLE ioftdata14_zd         	: std_logic := 'X';
    VARIABLE ioftdata14_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    ioftdata14_zd 	:= ioftdata14_out;

    VitalPathDelay01Z (

        OutSignal => ioftdata14, OutSignalName => "ioftdata14", OutTemp => ioftdata14_zd,
      Paths      => (0 => (InputChangeTime => PADDT_ipd'last_event,
                           PathDelay => tpd_PADDT_ioftdata14,
                           PathCondition => TRUE)),
      GlitchData => ioftdata14_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity io_ft_data_13_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity io_ft_data_13_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "io_ft_data_13_B";

      tipd_PADDT  	: VitalDelayType01 := (0 ns, 0 ns);

        tpd_PADDT_ioftdata13	 : VitalDelayType01Z := (0 ns, 0 ns, 0 ns , 0 ns, 0 ns, 0 ns)
        );

    port (PADDT: in Std_logic; ioftdata13: out Std_logic);

    ATTRIBUTE Vital_Level0 OF io_ft_data_13_B : ENTITY IS TRUE;

  end io_ft_data_13_B;

  architecture Structure of io_ft_data_13_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDT_ipd 	: std_logic := 'X';
    signal ioftdata13_out 	: std_logic := 'X';

    signal GNDI: Std_logic;
    signal PADDT_NOTIN: Std_logic;
    component sapiobuf
      port (I: in Std_logic; T: in Std_logic; PAD: out Std_logic);
    end component;
    component gnd
      port (PWR0: out Std_logic);
    end component;
    component inverter
      port (I: in Std_logic; Z: out Std_logic);
    end component;
  begin
    io_ft_data_pad_13: sapiobuf
      port map (I=>GNDI, T=>PADDT_NOTIN, PAD=>ioftdata13_out);
    DRIVEGND: gnd
      port map (PWR0=>GNDI);
    PADDT_INVERTERIN: inverter
      port map (I=>PADDT_ipd, Z=>PADDT_NOTIN);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDT_ipd, PADDT, tipd_PADDT);
    END BLOCK;

    VitalBehavior : PROCESS (PADDT_ipd, ioftdata13_out)
    VARIABLE ioftdata13_zd         	: std_logic := 'X';
    VARIABLE ioftdata13_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    ioftdata13_zd 	:= ioftdata13_out;

    VitalPathDelay01Z (

        OutSignal => ioftdata13, OutSignalName => "ioftdata13", OutTemp => ioftdata13_zd,
      Paths      => (0 => (InputChangeTime => PADDT_ipd'last_event,
                           PathDelay => tpd_PADDT_ioftdata13,
                           PathCondition => TRUE)),
      GlitchData => ioftdata13_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity io_ft_data_12_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity io_ft_data_12_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "io_ft_data_12_B";

      tipd_PADDT  	: VitalDelayType01 := (0 ns, 0 ns);

        tpd_PADDT_ioftdata12	 : VitalDelayType01Z := (0 ns, 0 ns, 0 ns , 0 ns, 0 ns, 0 ns)
        );

    port (PADDT: in Std_logic; ioftdata12: out Std_logic);

    ATTRIBUTE Vital_Level0 OF io_ft_data_12_B : ENTITY IS TRUE;

  end io_ft_data_12_B;

  architecture Structure of io_ft_data_12_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDT_ipd 	: std_logic := 'X';
    signal ioftdata12_out 	: std_logic := 'X';

    signal GNDI: Std_logic;
    signal PADDT_NOTIN: Std_logic;
    component sapiobuf
      port (I: in Std_logic; T: in Std_logic; PAD: out Std_logic);
    end component;
    component gnd
      port (PWR0: out Std_logic);
    end component;
    component inverter
      port (I: in Std_logic; Z: out Std_logic);
    end component;
  begin
    io_ft_data_pad_12: sapiobuf
      port map (I=>GNDI, T=>PADDT_NOTIN, PAD=>ioftdata12_out);
    DRIVEGND: gnd
      port map (PWR0=>GNDI);
    PADDT_INVERTERIN: inverter
      port map (I=>PADDT_ipd, Z=>PADDT_NOTIN);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDT_ipd, PADDT, tipd_PADDT);
    END BLOCK;

    VitalBehavior : PROCESS (PADDT_ipd, ioftdata12_out)
    VARIABLE ioftdata12_zd         	: std_logic := 'X';
    VARIABLE ioftdata12_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    ioftdata12_zd 	:= ioftdata12_out;

    VitalPathDelay01Z (

        OutSignal => ioftdata12, OutSignalName => "ioftdata12", OutTemp => ioftdata12_zd,
      Paths      => (0 => (InputChangeTime => PADDT_ipd'last_event,
                           PathDelay => tpd_PADDT_ioftdata12,
                           PathCondition => TRUE)),
      GlitchData => ioftdata12_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity io_ft_data_11_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity io_ft_data_11_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "io_ft_data_11_B";

      tipd_PADDT  	: VitalDelayType01 := (0 ns, 0 ns);

        tpd_PADDT_ioftdata11	 : VitalDelayType01Z := (0 ns, 0 ns, 0 ns , 0 ns, 0 ns, 0 ns)
        );

    port (PADDT: in Std_logic; ioftdata11: out Std_logic);

    ATTRIBUTE Vital_Level0 OF io_ft_data_11_B : ENTITY IS TRUE;

  end io_ft_data_11_B;

  architecture Structure of io_ft_data_11_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDT_ipd 	: std_logic := 'X';
    signal ioftdata11_out 	: std_logic := 'X';

    signal GNDI: Std_logic;
    signal PADDT_NOTIN: Std_logic;
    component sapiobuf
      port (I: in Std_logic; T: in Std_logic; PAD: out Std_logic);
    end component;
    component gnd
      port (PWR0: out Std_logic);
    end component;
    component inverter
      port (I: in Std_logic; Z: out Std_logic);
    end component;
  begin
    io_ft_data_pad_11: sapiobuf
      port map (I=>GNDI, T=>PADDT_NOTIN, PAD=>ioftdata11_out);
    DRIVEGND: gnd
      port map (PWR0=>GNDI);
    PADDT_INVERTERIN: inverter
      port map (I=>PADDT_ipd, Z=>PADDT_NOTIN);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDT_ipd, PADDT, tipd_PADDT);
    END BLOCK;

    VitalBehavior : PROCESS (PADDT_ipd, ioftdata11_out)
    VARIABLE ioftdata11_zd         	: std_logic := 'X';
    VARIABLE ioftdata11_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    ioftdata11_zd 	:= ioftdata11_out;

    VitalPathDelay01Z (

        OutSignal => ioftdata11, OutSignalName => "ioftdata11", OutTemp => ioftdata11_zd,
      Paths      => (0 => (InputChangeTime => PADDT_ipd'last_event,
                           PathDelay => tpd_PADDT_ioftdata11,
                           PathCondition => TRUE)),
      GlitchData => ioftdata11_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity io_ft_data_10_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity io_ft_data_10_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "io_ft_data_10_B";

      tipd_PADDT  	: VitalDelayType01 := (0 ns, 0 ns);

        tpd_PADDT_ioftdata10	 : VitalDelayType01Z := (0 ns, 0 ns, 0 ns , 0 ns, 0 ns, 0 ns)
        );

    port (PADDT: in Std_logic; ioftdata10: out Std_logic);

    ATTRIBUTE Vital_Level0 OF io_ft_data_10_B : ENTITY IS TRUE;

  end io_ft_data_10_B;

  architecture Structure of io_ft_data_10_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDT_ipd 	: std_logic := 'X';
    signal ioftdata10_out 	: std_logic := 'X';

    signal GNDI: Std_logic;
    signal PADDT_NOTIN: Std_logic;
    component sapiobuf
      port (I: in Std_logic; T: in Std_logic; PAD: out Std_logic);
    end component;
    component gnd
      port (PWR0: out Std_logic);
    end component;
    component inverter
      port (I: in Std_logic; Z: out Std_logic);
    end component;
  begin
    io_ft_data_pad_10: sapiobuf
      port map (I=>GNDI, T=>PADDT_NOTIN, PAD=>ioftdata10_out);
    DRIVEGND: gnd
      port map (PWR0=>GNDI);
    PADDT_INVERTERIN: inverter
      port map (I=>PADDT_ipd, Z=>PADDT_NOTIN);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDT_ipd, PADDT, tipd_PADDT);
    END BLOCK;

    VitalBehavior : PROCESS (PADDT_ipd, ioftdata10_out)
    VARIABLE ioftdata10_zd         	: std_logic := 'X';
    VARIABLE ioftdata10_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    ioftdata10_zd 	:= ioftdata10_out;

    VitalPathDelay01Z (

        OutSignal => ioftdata10, OutSignalName => "ioftdata10", OutTemp => ioftdata10_zd,
      Paths      => (0 => (InputChangeTime => PADDT_ipd'last_event,
                           PathDelay => tpd_PADDT_ioftdata10,
                           PathCondition => TRUE)),
      GlitchData => ioftdata10_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity io_ft_data_9_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity io_ft_data_9_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "io_ft_data_9_B";

      tipd_PADDT  	: VitalDelayType01 := (0 ns, 0 ns);

        tpd_PADDT_ioftdata9	 : VitalDelayType01Z := (0 ns, 0 ns, 0 ns , 0 ns, 0 ns, 0 ns)
        );

    port (PADDT: in Std_logic; ioftdata9: out Std_logic);

    ATTRIBUTE Vital_Level0 OF io_ft_data_9_B : ENTITY IS TRUE;

  end io_ft_data_9_B;

  architecture Structure of io_ft_data_9_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDT_ipd 	: std_logic := 'X';
    signal ioftdata9_out 	: std_logic := 'X';

    signal GNDI: Std_logic;
    signal PADDT_NOTIN: Std_logic;
    component sapiobuf
      port (I: in Std_logic; T: in Std_logic; PAD: out Std_logic);
    end component;
    component gnd
      port (PWR0: out Std_logic);
    end component;
    component inverter
      port (I: in Std_logic; Z: out Std_logic);
    end component;
  begin
    io_ft_data_pad_9: sapiobuf
      port map (I=>GNDI, T=>PADDT_NOTIN, PAD=>ioftdata9_out);
    DRIVEGND: gnd
      port map (PWR0=>GNDI);
    PADDT_INVERTERIN: inverter
      port map (I=>PADDT_ipd, Z=>PADDT_NOTIN);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDT_ipd, PADDT, tipd_PADDT);
    END BLOCK;

    VitalBehavior : PROCESS (PADDT_ipd, ioftdata9_out)
    VARIABLE ioftdata9_zd         	: std_logic := 'X';
    VARIABLE ioftdata9_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    ioftdata9_zd 	:= ioftdata9_out;

    VitalPathDelay01Z (
      OutSignal => ioftdata9, OutSignalName => "ioftdata9", OutTemp => ioftdata9_zd,
      Paths      => (0 => (InputChangeTime => PADDT_ipd'last_event,
                           PathDelay => tpd_PADDT_ioftdata9,
                           PathCondition => TRUE)),
      GlitchData => ioftdata9_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity io_ft_data_8_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity io_ft_data_8_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "io_ft_data_8_B";

      tipd_PADDT  	: VitalDelayType01 := (0 ns, 0 ns);

        tpd_PADDT_ioftdata8	 : VitalDelayType01Z := (0 ns, 0 ns, 0 ns , 0 ns, 0 ns, 0 ns)
        );

    port (PADDT: in Std_logic; ioftdata8: out Std_logic);

    ATTRIBUTE Vital_Level0 OF io_ft_data_8_B : ENTITY IS TRUE;

  end io_ft_data_8_B;

  architecture Structure of io_ft_data_8_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDT_ipd 	: std_logic := 'X';
    signal ioftdata8_out 	: std_logic := 'X';

    signal GNDI: Std_logic;
    signal PADDT_NOTIN: Std_logic;
    component sapiobuf
      port (I: in Std_logic; T: in Std_logic; PAD: out Std_logic);
    end component;
    component gnd
      port (PWR0: out Std_logic);
    end component;
    component inverter
      port (I: in Std_logic; Z: out Std_logic);
    end component;
  begin
    io_ft_data_pad_8: sapiobuf
      port map (I=>GNDI, T=>PADDT_NOTIN, PAD=>ioftdata8_out);
    DRIVEGND: gnd
      port map (PWR0=>GNDI);
    PADDT_INVERTERIN: inverter
      port map (I=>PADDT_ipd, Z=>PADDT_NOTIN);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDT_ipd, PADDT, tipd_PADDT);
    END BLOCK;

    VitalBehavior : PROCESS (PADDT_ipd, ioftdata8_out)
    VARIABLE ioftdata8_zd         	: std_logic := 'X';
    VARIABLE ioftdata8_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    ioftdata8_zd 	:= ioftdata8_out;

    VitalPathDelay01Z (
      OutSignal => ioftdata8, OutSignalName => "ioftdata8", OutTemp => ioftdata8_zd,
      Paths      => (0 => (InputChangeTime => PADDT_ipd'last_event,
                           PathDelay => tpd_PADDT_ioftdata8,
                           PathCondition => TRUE)),
      GlitchData => ioftdata8_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity vcc
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity vcc is
    port (PWR1: out Std_logic);

    ATTRIBUTE Vital_Level0 OF vcc : ENTITY IS TRUE;

  end vcc;

  architecture Structure of vcc is
  begin
    INST1: VHI
      port map (Z=>PWR1);
  end Structure;

-- entity io_ft_data_7_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity io_ft_data_7_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "io_ft_data_7_B";

      tipd_PADDT  	: VitalDelayType01 := (0 ns, 0 ns);

        tpd_PADDT_ioftdata7	 : VitalDelayType01Z := (0 ns, 0 ns, 0 ns , 0 ns, 0 ns, 0 ns)
        );

    port (PADDT: in Std_logic; ioftdata7: out Std_logic);

    ATTRIBUTE Vital_Level0 OF io_ft_data_7_B : ENTITY IS TRUE;

  end io_ft_data_7_B;

  architecture Structure of io_ft_data_7_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDT_ipd 	: std_logic := 'X';
    signal ioftdata7_out 	: std_logic := 'X';

    signal VCCI: Std_logic;
    signal PADDT_NOTIN: Std_logic;
    component sapiobuf
      port (I: in Std_logic; T: in Std_logic; PAD: out Std_logic);
    end component;
    component inverter
      port (I: in Std_logic; Z: out Std_logic);
    end component;
    component vcc
      port (PWR1: out Std_logic);
    end component;
  begin
    io_ft_data_pad_7: sapiobuf
      port map (I=>VCCI, T=>PADDT_NOTIN, PAD=>ioftdata7_out);
    DRIVEVCC: vcc
      port map (PWR1=>VCCI);
    PADDT_INVERTERIN: inverter
      port map (I=>PADDT_ipd, Z=>PADDT_NOTIN);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDT_ipd, PADDT, tipd_PADDT);
    END BLOCK;

    VitalBehavior : PROCESS (PADDT_ipd, ioftdata7_out)
    VARIABLE ioftdata7_zd         	: std_logic := 'X';
    VARIABLE ioftdata7_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    ioftdata7_zd 	:= ioftdata7_out;

    VitalPathDelay01Z (
      OutSignal => ioftdata7, OutSignalName => "ioftdata7", OutTemp => ioftdata7_zd,
      Paths      => (0 => (InputChangeTime => PADDT_ipd'last_event,
                           PathDelay => tpd_PADDT_ioftdata7,
                           PathCondition => TRUE)),
      GlitchData => ioftdata7_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity io_ft_data_6_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity io_ft_data_6_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "io_ft_data_6_B";

      tipd_PADDT  	: VitalDelayType01 := (0 ns, 0 ns);

        tpd_PADDT_ioftdata6	 : VitalDelayType01Z := (0 ns, 0 ns, 0 ns , 0 ns, 0 ns, 0 ns)
        );

    port (PADDT: in Std_logic; ioftdata6: out Std_logic);

    ATTRIBUTE Vital_Level0 OF io_ft_data_6_B : ENTITY IS TRUE;

  end io_ft_data_6_B;

  architecture Structure of io_ft_data_6_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDT_ipd 	: std_logic := 'X';
    signal ioftdata6_out 	: std_logic := 'X';

    signal VCCI: Std_logic;
    signal PADDT_NOTIN: Std_logic;
    component sapiobuf
      port (I: in Std_logic; T: in Std_logic; PAD: out Std_logic);
    end component;
    component inverter
      port (I: in Std_logic; Z: out Std_logic);
    end component;
    component vcc
      port (PWR1: out Std_logic);
    end component;
  begin
    io_ft_data_pad_6: sapiobuf
      port map (I=>VCCI, T=>PADDT_NOTIN, PAD=>ioftdata6_out);
    DRIVEVCC: vcc
      port map (PWR1=>VCCI);
    PADDT_INVERTERIN: inverter
      port map (I=>PADDT_ipd, Z=>PADDT_NOTIN);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDT_ipd, PADDT, tipd_PADDT);
    END BLOCK;

    VitalBehavior : PROCESS (PADDT_ipd, ioftdata6_out)
    VARIABLE ioftdata6_zd         	: std_logic := 'X';
    VARIABLE ioftdata6_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    ioftdata6_zd 	:= ioftdata6_out;

    VitalPathDelay01Z (
      OutSignal => ioftdata6, OutSignalName => "ioftdata6", OutTemp => ioftdata6_zd,
      Paths      => (0 => (InputChangeTime => PADDT_ipd'last_event,
                           PathDelay => tpd_PADDT_ioftdata6,
                           PathCondition => TRUE)),
      GlitchData => ioftdata6_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity io_ft_data_5_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity io_ft_data_5_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "io_ft_data_5_B";

      tipd_PADDT  	: VitalDelayType01 := (0 ns, 0 ns);

        tpd_PADDT_ioftdata5	 : VitalDelayType01Z := (0 ns, 0 ns, 0 ns , 0 ns, 0 ns, 0 ns)
        );

    port (PADDT: in Std_logic; ioftdata5: out Std_logic);

    ATTRIBUTE Vital_Level0 OF io_ft_data_5_B : ENTITY IS TRUE;

  end io_ft_data_5_B;

  architecture Structure of io_ft_data_5_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDT_ipd 	: std_logic := 'X';
    signal ioftdata5_out 	: std_logic := 'X';

    signal VCCI: Std_logic;
    signal PADDT_NOTIN: Std_logic;
    component sapiobuf
      port (I: in Std_logic; T: in Std_logic; PAD: out Std_logic);
    end component;
    component inverter
      port (I: in Std_logic; Z: out Std_logic);
    end component;
    component vcc
      port (PWR1: out Std_logic);
    end component;
  begin
    io_ft_data_pad_5: sapiobuf
      port map (I=>VCCI, T=>PADDT_NOTIN, PAD=>ioftdata5_out);
    DRIVEVCC: vcc
      port map (PWR1=>VCCI);
    PADDT_INVERTERIN: inverter
      port map (I=>PADDT_ipd, Z=>PADDT_NOTIN);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDT_ipd, PADDT, tipd_PADDT);
    END BLOCK;

    VitalBehavior : PROCESS (PADDT_ipd, ioftdata5_out)
    VARIABLE ioftdata5_zd         	: std_logic := 'X';
    VARIABLE ioftdata5_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    ioftdata5_zd 	:= ioftdata5_out;

    VitalPathDelay01Z (
      OutSignal => ioftdata5, OutSignalName => "ioftdata5", OutTemp => ioftdata5_zd,
      Paths      => (0 => (InputChangeTime => PADDT_ipd'last_event,
                           PathDelay => tpd_PADDT_ioftdata5,
                           PathCondition => TRUE)),
      GlitchData => ioftdata5_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity io_ft_data_4_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity io_ft_data_4_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "io_ft_data_4_B";

      tipd_PADDT  	: VitalDelayType01 := (0 ns, 0 ns);

        tpd_PADDT_ioftdata4	 : VitalDelayType01Z := (0 ns, 0 ns, 0 ns , 0 ns, 0 ns, 0 ns)
        );

    port (PADDT: in Std_logic; ioftdata4: out Std_logic);

    ATTRIBUTE Vital_Level0 OF io_ft_data_4_B : ENTITY IS TRUE;

  end io_ft_data_4_B;

  architecture Structure of io_ft_data_4_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDT_ipd 	: std_logic := 'X';
    signal ioftdata4_out 	: std_logic := 'X';

    signal VCCI: Std_logic;
    signal PADDT_NOTIN: Std_logic;
    component sapiobuf
      port (I: in Std_logic; T: in Std_logic; PAD: out Std_logic);
    end component;
    component inverter
      port (I: in Std_logic; Z: out Std_logic);
    end component;
    component vcc
      port (PWR1: out Std_logic);
    end component;
  begin
    io_ft_data_pad_4: sapiobuf
      port map (I=>VCCI, T=>PADDT_NOTIN, PAD=>ioftdata4_out);
    DRIVEVCC: vcc
      port map (PWR1=>VCCI);
    PADDT_INVERTERIN: inverter
      port map (I=>PADDT_ipd, Z=>PADDT_NOTIN);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDT_ipd, PADDT, tipd_PADDT);
    END BLOCK;

    VitalBehavior : PROCESS (PADDT_ipd, ioftdata4_out)
    VARIABLE ioftdata4_zd         	: std_logic := 'X';
    VARIABLE ioftdata4_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    ioftdata4_zd 	:= ioftdata4_out;

    VitalPathDelay01Z (
      OutSignal => ioftdata4, OutSignalName => "ioftdata4", OutTemp => ioftdata4_zd,
      Paths      => (0 => (InputChangeTime => PADDT_ipd'last_event,
                           PathDelay => tpd_PADDT_ioftdata4,
                           PathCondition => TRUE)),
      GlitchData => ioftdata4_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity io_ft_data_3_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity io_ft_data_3_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "io_ft_data_3_B";

      tipd_PADDT  	: VitalDelayType01 := (0 ns, 0 ns);

        tpd_PADDT_ioftdata3	 : VitalDelayType01Z := (0 ns, 0 ns, 0 ns , 0 ns, 0 ns, 0 ns)
        );

    port (PADDT: in Std_logic; ioftdata3: out Std_logic);

    ATTRIBUTE Vital_Level0 OF io_ft_data_3_B : ENTITY IS TRUE;

  end io_ft_data_3_B;

  architecture Structure of io_ft_data_3_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDT_ipd 	: std_logic := 'X';
    signal ioftdata3_out 	: std_logic := 'X';

    signal VCCI: Std_logic;
    signal PADDT_NOTIN: Std_logic;
    component sapiobuf
      port (I: in Std_logic; T: in Std_logic; PAD: out Std_logic);
    end component;
    component inverter
      port (I: in Std_logic; Z: out Std_logic);
    end component;
    component vcc
      port (PWR1: out Std_logic);
    end component;
  begin
    io_ft_data_pad_3: sapiobuf
      port map (I=>VCCI, T=>PADDT_NOTIN, PAD=>ioftdata3_out);
    DRIVEVCC: vcc
      port map (PWR1=>VCCI);
    PADDT_INVERTERIN: inverter
      port map (I=>PADDT_ipd, Z=>PADDT_NOTIN);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDT_ipd, PADDT, tipd_PADDT);
    END BLOCK;

    VitalBehavior : PROCESS (PADDT_ipd, ioftdata3_out)
    VARIABLE ioftdata3_zd         	: std_logic := 'X';
    VARIABLE ioftdata3_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    ioftdata3_zd 	:= ioftdata3_out;

    VitalPathDelay01Z (
      OutSignal => ioftdata3, OutSignalName => "ioftdata3", OutTemp => ioftdata3_zd,
      Paths      => (0 => (InputChangeTime => PADDT_ipd'last_event,
                           PathDelay => tpd_PADDT_ioftdata3,
                           PathCondition => TRUE)),
      GlitchData => ioftdata3_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity io_ft_data_2_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity io_ft_data_2_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "io_ft_data_2_B";

      tipd_PADDT  	: VitalDelayType01 := (0 ns, 0 ns);

        tpd_PADDT_ioftdata2	 : VitalDelayType01Z := (0 ns, 0 ns, 0 ns , 0 ns, 0 ns, 0 ns)
        );

    port (PADDT: in Std_logic; ioftdata2: out Std_logic);

    ATTRIBUTE Vital_Level0 OF io_ft_data_2_B : ENTITY IS TRUE;

  end io_ft_data_2_B;

  architecture Structure of io_ft_data_2_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDT_ipd 	: std_logic := 'X';
    signal ioftdata2_out 	: std_logic := 'X';

    signal VCCI: Std_logic;
    signal PADDT_NOTIN: Std_logic;
    component sapiobuf
      port (I: in Std_logic; T: in Std_logic; PAD: out Std_logic);
    end component;
    component inverter
      port (I: in Std_logic; Z: out Std_logic);
    end component;
    component vcc
      port (PWR1: out Std_logic);
    end component;
  begin
    io_ft_data_pad_2: sapiobuf
      port map (I=>VCCI, T=>PADDT_NOTIN, PAD=>ioftdata2_out);
    DRIVEVCC: vcc
      port map (PWR1=>VCCI);
    PADDT_INVERTERIN: inverter
      port map (I=>PADDT_ipd, Z=>PADDT_NOTIN);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDT_ipd, PADDT, tipd_PADDT);
    END BLOCK;

    VitalBehavior : PROCESS (PADDT_ipd, ioftdata2_out)
    VARIABLE ioftdata2_zd         	: std_logic := 'X';
    VARIABLE ioftdata2_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    ioftdata2_zd 	:= ioftdata2_out;

    VitalPathDelay01Z (
      OutSignal => ioftdata2, OutSignalName => "ioftdata2", OutTemp => ioftdata2_zd,
      Paths      => (0 => (InputChangeTime => PADDT_ipd'last_event,
                           PathDelay => tpd_PADDT_ioftdata2,
                           PathCondition => TRUE)),
      GlitchData => ioftdata2_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity io_ft_data_1_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity io_ft_data_1_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "io_ft_data_1_B";

      tipd_PADDT  	: VitalDelayType01 := (0 ns, 0 ns);

        tpd_PADDT_ioftdata1	 : VitalDelayType01Z := (0 ns, 0 ns, 0 ns , 0 ns, 0 ns, 0 ns)
        );

    port (PADDT: in Std_logic; ioftdata1: out Std_logic);

    ATTRIBUTE Vital_Level0 OF io_ft_data_1_B : ENTITY IS TRUE;

  end io_ft_data_1_B;

  architecture Structure of io_ft_data_1_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDT_ipd 	: std_logic := 'X';
    signal ioftdata1_out 	: std_logic := 'X';

    signal VCCI: Std_logic;
    signal PADDT_NOTIN: Std_logic;
    component sapiobuf
      port (I: in Std_logic; T: in Std_logic; PAD: out Std_logic);
    end component;
    component inverter
      port (I: in Std_logic; Z: out Std_logic);
    end component;
    component vcc
      port (PWR1: out Std_logic);
    end component;
  begin
    io_ft_data_pad_1: sapiobuf
      port map (I=>VCCI, T=>PADDT_NOTIN, PAD=>ioftdata1_out);
    DRIVEVCC: vcc
      port map (PWR1=>VCCI);
    PADDT_INVERTERIN: inverter
      port map (I=>PADDT_ipd, Z=>PADDT_NOTIN);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDT_ipd, PADDT, tipd_PADDT);
    END BLOCK;

    VitalBehavior : PROCESS (PADDT_ipd, ioftdata1_out)
    VARIABLE ioftdata1_zd         	: std_logic := 'X';
    VARIABLE ioftdata1_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    ioftdata1_zd 	:= ioftdata1_out;

    VitalPathDelay01Z (
      OutSignal => ioftdata1, OutSignalName => "ioftdata1", OutTemp => ioftdata1_zd,
      Paths      => (0 => (InputChangeTime => PADDT_ipd'last_event,
                           PathDelay => tpd_PADDT_ioftdata1,
                           PathCondition => TRUE)),
      GlitchData => ioftdata1_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity io_ft_data_0_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity io_ft_data_0_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "io_ft_data_0_B";

      tipd_PADDT  	: VitalDelayType01 := (0 ns, 0 ns);

        tpd_PADDT_ioftdata0	 : VitalDelayType01Z := (0 ns, 0 ns, 0 ns , 0 ns, 0 ns, 0 ns)
        );

    port (PADDT: in Std_logic; ioftdata0: out Std_logic);

    ATTRIBUTE Vital_Level0 OF io_ft_data_0_B : ENTITY IS TRUE;

  end io_ft_data_0_B;

  architecture Structure of io_ft_data_0_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDT_ipd 	: std_logic := 'X';
    signal ioftdata0_out 	: std_logic := 'X';

    signal VCCI: Std_logic;
    signal PADDT_NOTIN: Std_logic;
    component sapiobuf
      port (I: in Std_logic; T: in Std_logic; PAD: out Std_logic);
    end component;
    component inverter
      port (I: in Std_logic; Z: out Std_logic);
    end component;
    component vcc
      port (PWR1: out Std_logic);
    end component;
  begin
    io_ft_data_pad_0: sapiobuf
      port map (I=>VCCI, T=>PADDT_NOTIN, PAD=>ioftdata0_out);
    DRIVEVCC: vcc
      port map (PWR1=>VCCI);
    PADDT_INVERTERIN: inverter
      port map (I=>PADDT_ipd, Z=>PADDT_NOTIN);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDT_ipd, PADDT, tipd_PADDT);
    END BLOCK;

    VitalBehavior : PROCESS (PADDT_ipd, ioftdata0_out)
    VARIABLE ioftdata0_zd         	: std_logic := 'X';
    VARIABLE ioftdata0_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    ioftdata0_zd 	:= ioftdata0_out;

    VitalPathDelay01Z (
      OutSignal => ioftdata0, OutSignalName => "ioftdata0", OutTemp => ioftdata0_zd,
      Paths      => (0 => (InputChangeTime => PADDT_ipd'last_event,
                           PathDelay => tpd_PADDT_ioftdata0,
                           PathCondition => TRUE)),
      GlitchData => ioftdata0_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity sapiobuf0001
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity sapiobuf0001 is
    port (I: in Std_logic; PAD: out Std_logic);

    ATTRIBUTE Vital_Level0 OF sapiobuf0001 : ENTITY IS TRUE;

  end sapiobuf0001;

  architecture Structure of sapiobuf0001 is
  begin
    INST5: OB
      port map (I=>I, O=>PAD);
  end Structure;

-- entity o_ft_wr_nB
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity o_ft_wr_nB is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "o_ft_wr_nB";

      tipd_PADDO  	: VitalDelayType01 := (0 ns, 0 ns);
      tpd_PADDO_oftwrn	 : VitalDelayType01 := (0 ns, 0 ns));

    port (PADDO: in Std_logic; oftwrn: out Std_logic);

    ATTRIBUTE Vital_Level0 OF o_ft_wr_nB : ENTITY IS TRUE;

  end o_ft_wr_nB;

  architecture Structure of o_ft_wr_nB is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDO_ipd 	: std_logic := 'X';
    signal oftwrn_out 	: std_logic := 'X';

    component sapiobuf0001
      port (I: in Std_logic; PAD: out Std_logic);
    end component;
  begin
    o_ft_wr_n_pad: sapiobuf0001
      port map (I=>PADDO_ipd, PAD=>oftwrn_out);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDO_ipd, PADDO, tipd_PADDO);
    END BLOCK;

    VitalBehavior : PROCESS (PADDO_ipd, oftwrn_out)
    VARIABLE oftwrn_zd         	: std_logic := 'X';
    VARIABLE oftwrn_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    oftwrn_zd 	:= oftwrn_out;

    VitalPathDelay01 (
      OutSignal => oftwrn, OutSignalName => "oftwrn", OutTemp => oftwrn_zd,
      Paths      => (0 => (InputChangeTime => PADDO_ipd'last_event,
                           PathDelay => tpd_PADDO_oftwrn,
                           PathCondition => TRUE)),
      GlitchData => oftwrn_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity o_ft_rd_nB
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity o_ft_rd_nB is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "o_ft_rd_nB";

      tipd_PADDO  	: VitalDelayType01 := (0 ns, 0 ns);
      tpd_PADDO_oftrdn	 : VitalDelayType01 := (0 ns, 0 ns));

    port (PADDO: in Std_logic; oftrdn: out Std_logic);

    ATTRIBUTE Vital_Level0 OF o_ft_rd_nB : ENTITY IS TRUE;

  end o_ft_rd_nB;

  architecture Structure of o_ft_rd_nB is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDO_ipd 	: std_logic := 'X';
    signal oftrdn_out 	: std_logic := 'X';

    component sapiobuf0001
      port (I: in Std_logic; PAD: out Std_logic);
    end component;
  begin
    o_ft_rd_n_pad: sapiobuf0001
      port map (I=>PADDO_ipd, PAD=>oftrdn_out);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDO_ipd, PADDO, tipd_PADDO);
    END BLOCK;

    VitalBehavior : PROCESS (PADDO_ipd, oftrdn_out)
    VARIABLE oftrdn_zd         	: std_logic := 'X';
    VARIABLE oftrdn_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    oftrdn_zd 	:= oftrdn_out;

    VitalPathDelay01 (
      OutSignal => oftrdn, OutSignalName => "oftrdn", OutTemp => oftrdn_zd,
      Paths      => (0 => (InputChangeTime => PADDO_ipd'last_event,
                           PathDelay => tpd_PADDO_oftrdn,
                           PathCondition => TRUE)),
      GlitchData => oftrdn_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity io_ft_oe_nB
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity io_ft_oe_nB is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "io_ft_oe_nB";

      tipd_PADDO  	: VitalDelayType01 := (0 ns, 0 ns);
      tpd_PADDO_ioftoen	 : VitalDelayType01 := (0 ns, 0 ns));

    port (PADDO: in Std_logic; ioftoen: out Std_logic);

    ATTRIBUTE Vital_Level0 OF io_ft_oe_nB : ENTITY IS TRUE;

  end io_ft_oe_nB;

  architecture Structure of io_ft_oe_nB is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDO_ipd 	: std_logic := 'X';
    signal ioftoen_out 	: std_logic := 'X';

    component sapiobuf0001
      port (I: in Std_logic; PAD: out Std_logic);
    end component;
  begin
    io_ft_oe_n_pad: sapiobuf0001
      port map (I=>PADDO_ipd, PAD=>ioftoen_out);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDO_ipd, PADDO, tipd_PADDO);
    END BLOCK;

    VitalBehavior : PROCESS (PADDO_ipd, ioftoen_out)
    VARIABLE ioftoen_zd         	: std_logic := 'X';
    VARIABLE ioftoen_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    ioftoen_zd 	:= ioftoen_out;

    VitalPathDelay01 (
      OutSignal => ioftoen, OutSignalName => "ioftoen", OutTemp => ioftoen_zd,
      Paths      => (0 => (InputChangeTime => PADDO_ipd'last_event,
                           PathDelay => tpd_PADDO_ioftoen,
                           PathCondition => TRUE)),
      GlitchData => ioftoen_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity o_leds_7_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity o_leds_7_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "o_leds_7_B");

    port (oleds7: out Std_logic);

    ATTRIBUTE Vital_Level0 OF o_leds_7_B : ENTITY IS TRUE;

  end o_leds_7_B;

  architecture Structure of o_leds_7_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal oleds7_out 	: std_logic := 'X';

    signal GNDI: Std_logic;
    component gnd
      port (PWR0: out Std_logic);
    end component;
    component sapiobuf0001
      port (I: in Std_logic; PAD: out Std_logic);
    end component;
  begin
    o_leds_pad_7: sapiobuf0001
      port map (I=>GNDI, PAD=>oleds7_out);
    DRIVEGND: gnd
      port map (PWR0=>GNDI);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
    END BLOCK;

    VitalBehavior : PROCESS (oleds7_out)


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    oleds7 	<= oleds7_out;


    END PROCESS;

  end Structure;

-- entity o_leds_6_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity o_leds_6_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "o_leds_6_B";

      tipd_PADDO  	: VitalDelayType01 := (0 ns, 0 ns);
      tpd_PADDO_oleds6	 : VitalDelayType01 := (0 ns, 0 ns));

    port (PADDO: in Std_logic; oleds6: out Std_logic);

    ATTRIBUTE Vital_Level0 OF o_leds_6_B : ENTITY IS TRUE;

  end o_leds_6_B;

  architecture Structure of o_leds_6_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDO_ipd 	: std_logic := 'X';
    signal oleds6_out 	: std_logic := 'X';

    component sapiobuf0001
      port (I: in Std_logic; PAD: out Std_logic);
    end component;
  begin
    o_leds_pad_6: sapiobuf0001
      port map (I=>PADDO_ipd, PAD=>oleds6_out);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDO_ipd, PADDO, tipd_PADDO);
    END BLOCK;

    VitalBehavior : PROCESS (PADDO_ipd, oleds6_out)
    VARIABLE oleds6_zd         	: std_logic := 'X';
    VARIABLE oleds6_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    oleds6_zd 	:= oleds6_out;

    VitalPathDelay01 (
      OutSignal => oleds6, OutSignalName => "oleds6", OutTemp => oleds6_zd,
      Paths      => (0 => (InputChangeTime => PADDO_ipd'last_event,
                           PathDelay => tpd_PADDO_oleds6,
                           PathCondition => TRUE)),
      GlitchData => oleds6_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity o_leds_5_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity o_leds_5_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "o_leds_5_B";

      tipd_PADDO  	: VitalDelayType01 := (0 ns, 0 ns);
      tpd_PADDO_oleds5	 : VitalDelayType01 := (0 ns, 0 ns));

    port (PADDO: in Std_logic; oleds5: out Std_logic);

    ATTRIBUTE Vital_Level0 OF o_leds_5_B : ENTITY IS TRUE;

  end o_leds_5_B;

  architecture Structure of o_leds_5_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDO_ipd 	: std_logic := 'X';
    signal oleds5_out 	: std_logic := 'X';

    component sapiobuf0001
      port (I: in Std_logic; PAD: out Std_logic);
    end component;
  begin
    o_leds_pad_5: sapiobuf0001
      port map (I=>PADDO_ipd, PAD=>oleds5_out);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDO_ipd, PADDO, tipd_PADDO);
    END BLOCK;

    VitalBehavior : PROCESS (PADDO_ipd, oleds5_out)
    VARIABLE oleds5_zd         	: std_logic := 'X';
    VARIABLE oleds5_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    oleds5_zd 	:= oleds5_out;

    VitalPathDelay01 (
      OutSignal => oleds5, OutSignalName => "oleds5", OutTemp => oleds5_zd,
      Paths      => (0 => (InputChangeTime => PADDO_ipd'last_event,
                           PathDelay => tpd_PADDO_oleds5,
                           PathCondition => TRUE)),
      GlitchData => oleds5_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity o_leds_4_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity o_leds_4_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "o_leds_4_B";

      tipd_PADDO  	: VitalDelayType01 := (0 ns, 0 ns);
      tpd_PADDO_oleds4	 : VitalDelayType01 := (0 ns, 0 ns));

    port (PADDO: in Std_logic; oleds4: out Std_logic);

    ATTRIBUTE Vital_Level0 OF o_leds_4_B : ENTITY IS TRUE;

  end o_leds_4_B;

  architecture Structure of o_leds_4_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDO_ipd 	: std_logic := 'X';
    signal oleds4_out 	: std_logic := 'X';

    component sapiobuf0001
      port (I: in Std_logic; PAD: out Std_logic);
    end component;
  begin
    o_leds_pad_4: sapiobuf0001
      port map (I=>PADDO_ipd, PAD=>oleds4_out);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDO_ipd, PADDO, tipd_PADDO);
    END BLOCK;

    VitalBehavior : PROCESS (PADDO_ipd, oleds4_out)
    VARIABLE oleds4_zd         	: std_logic := 'X';
    VARIABLE oleds4_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    oleds4_zd 	:= oleds4_out;

    VitalPathDelay01 (
      OutSignal => oleds4, OutSignalName => "oleds4", OutTemp => oleds4_zd,
      Paths      => (0 => (InputChangeTime => PADDO_ipd'last_event,
                           PathDelay => tpd_PADDO_oleds4,
                           PathCondition => TRUE)),
      GlitchData => oleds4_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity o_leds_3_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity o_leds_3_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "o_leds_3_B";

      tipd_PADDO  	: VitalDelayType01 := (0 ns, 0 ns);
      tpd_PADDO_oleds3	 : VitalDelayType01 := (0 ns, 0 ns));

    port (PADDO: in Std_logic; oleds3: out Std_logic);

    ATTRIBUTE Vital_Level0 OF o_leds_3_B : ENTITY IS TRUE;

  end o_leds_3_B;

  architecture Structure of o_leds_3_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDO_ipd 	: std_logic := 'X';
    signal oleds3_out 	: std_logic := 'X';

    component sapiobuf0001
      port (I: in Std_logic; PAD: out Std_logic);
    end component;
  begin
    o_leds_pad_3: sapiobuf0001
      port map (I=>PADDO_ipd, PAD=>oleds3_out);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDO_ipd, PADDO, tipd_PADDO);
    END BLOCK;

    VitalBehavior : PROCESS (PADDO_ipd, oleds3_out)
    VARIABLE oleds3_zd         	: std_logic := 'X';
    VARIABLE oleds3_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    oleds3_zd 	:= oleds3_out;

    VitalPathDelay01 (
      OutSignal => oleds3, OutSignalName => "oleds3", OutTemp => oleds3_zd,
      Paths      => (0 => (InputChangeTime => PADDO_ipd'last_event,
                           PathDelay => tpd_PADDO_oleds3,
                           PathCondition => TRUE)),
      GlitchData => oleds3_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity o_leds_2_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity o_leds_2_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "o_leds_2_B";

      tipd_PADDO  	: VitalDelayType01 := (0 ns, 0 ns);
      tpd_PADDO_oleds2	 : VitalDelayType01 := (0 ns, 0 ns));

    port (PADDO: in Std_logic; oleds2: out Std_logic);

    ATTRIBUTE Vital_Level0 OF o_leds_2_B : ENTITY IS TRUE;

  end o_leds_2_B;

  architecture Structure of o_leds_2_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDO_ipd 	: std_logic := 'X';
    signal oleds2_out 	: std_logic := 'X';

    component sapiobuf0001
      port (I: in Std_logic; PAD: out Std_logic);
    end component;
  begin
    o_leds_pad_2: sapiobuf0001
      port map (I=>PADDO_ipd, PAD=>oleds2_out);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDO_ipd, PADDO, tipd_PADDO);
    END BLOCK;

    VitalBehavior : PROCESS (PADDO_ipd, oleds2_out)
    VARIABLE oleds2_zd         	: std_logic := 'X';
    VARIABLE oleds2_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    oleds2_zd 	:= oleds2_out;

    VitalPathDelay01 (
      OutSignal => oleds2, OutSignalName => "oleds2", OutTemp => oleds2_zd,
      Paths      => (0 => (InputChangeTime => PADDO_ipd'last_event,
                           PathDelay => tpd_PADDO_oleds2,
                           PathCondition => TRUE)),
      GlitchData => oleds2_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity o_leds_1_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity o_leds_1_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "o_leds_1_B";

      tipd_PADDO  	: VitalDelayType01 := (0 ns, 0 ns);
      tpd_PADDO_oleds1	 : VitalDelayType01 := (0 ns, 0 ns));

    port (PADDO: in Std_logic; oleds1: out Std_logic);

    ATTRIBUTE Vital_Level0 OF o_leds_1_B : ENTITY IS TRUE;

  end o_leds_1_B;

  architecture Structure of o_leds_1_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDO_ipd 	: std_logic := 'X';
    signal oleds1_out 	: std_logic := 'X';

    component sapiobuf0001
      port (I: in Std_logic; PAD: out Std_logic);
    end component;
  begin
    o_leds_pad_1: sapiobuf0001
      port map (I=>PADDO_ipd, PAD=>oleds1_out);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDO_ipd, PADDO, tipd_PADDO);
    END BLOCK;

    VitalBehavior : PROCESS (PADDO_ipd, oleds1_out)
    VARIABLE oleds1_zd         	: std_logic := 'X';
    VARIABLE oleds1_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    oleds1_zd 	:= oleds1_out;

    VitalPathDelay01 (
      OutSignal => oleds1, OutSignalName => "oleds1", OutTemp => oleds1_zd,
      Paths      => (0 => (InputChangeTime => PADDO_ipd'last_event,
                           PathDelay => tpd_PADDO_oleds1,
                           PathCondition => TRUE)),
      GlitchData => oleds1_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity o_leds_0_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity o_leds_0_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "o_leds_0_B";

      tipd_PADDO  	: VitalDelayType01 := (0 ns, 0 ns);
      tpd_PADDO_oleds0	 : VitalDelayType01 := (0 ns, 0 ns));

    port (PADDO: in Std_logic; oleds0: out Std_logic);

    ATTRIBUTE Vital_Level0 OF o_leds_0_B : ENTITY IS TRUE;

  end o_leds_0_B;

  architecture Structure of o_leds_0_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDO_ipd 	: std_logic := 'X';
    signal oleds0_out 	: std_logic := 'X';

    component sapiobuf0001
      port (I: in Std_logic; PAD: out Std_logic);
    end component;
  begin
    o_leds_pad_0: sapiobuf0001
      port map (I=>PADDO_ipd, PAD=>oleds0_out);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(PADDO_ipd, PADDO, tipd_PADDO);
    END BLOCK;

    VitalBehavior : PROCESS (PADDO_ipd, oleds0_out)
    VARIABLE oleds0_zd         	: std_logic := 'X';
    VARIABLE oleds0_GlitchData 	: VitalGlitchDataType;


    BEGIN

    IF (TimingChecksOn) THEN

    END IF;

    oleds0_zd 	:= oleds0_out;

    VitalPathDelay01 (
      OutSignal => oleds0, OutSignalName => "oleds0", OutTemp => oleds0_zd,
      Paths      => (0 => (InputChangeTime => PADDO_ipd'last_event,
                           PathDelay => tpd_PADDO_oleds0,
                           PathCondition => TRUE)),
      GlitchData => oleds0_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity sapiobuf0002
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity sapiobuf0002 is
    port (Z: out Std_logic; PAD: in Std_logic);

    ATTRIBUTE Vital_Level0 OF sapiobuf0002 : ENTITY IS TRUE;

  end sapiobuf0002;

  architecture Structure of sapiobuf0002 is
  begin
    INST1: IBPD
      port map (I=>PAD, O=>Z);
  end Structure;

-- entity i_clk16B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity i_clk16B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "i_clk16B";

      tipd_iclk16  	: VitalDelayType01 := (0 ns, 0 ns);
      tpd_iclk16_PADDI	 : VitalDelayType01 := (0 ns, 0 ns);
      tperiod_iclk16 	: VitalDelayType := 0 ns;
      tpw_iclk16_posedge	: VitalDelayType := 0 ns;
      tpw_iclk16_negedge	: VitalDelayType := 0 ns);

    port (PADDI: out Std_logic; iclk16: in Std_logic);

    ATTRIBUTE Vital_Level0 OF i_clk16B : ENTITY IS TRUE;

  end i_clk16B;

  architecture Structure of i_clk16B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDI_out 	: std_logic := 'X';
    signal iclk16_ipd 	: std_logic := 'X';

    component sapiobuf0002
      port (Z: out Std_logic; PAD: in Std_logic);
    end component;
  begin
    i_clk16_pad: sapiobuf0002
      port map (Z=>PADDI_out, PAD=>iclk16_ipd);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(iclk16_ipd, iclk16, tipd_iclk16);
    END BLOCK;

    VitalBehavior : PROCESS (PADDI_out, iclk16_ipd)
    VARIABLE PADDI_zd         	: std_logic := 'X';
    VARIABLE PADDI_GlitchData 	: VitalGlitchDataType;

    VARIABLE tviol_iclk16_iclk16          	: x01 := '0';
    VARIABLE periodcheckinfo_iclk16	: VitalPeriodDataType;

    BEGIN

    IF (TimingChecksOn) THEN
      VitalPeriodPulseCheck (
        TestSignal => iclk16_ipd,
        TestSignalName => "iclk16",
        Period => tperiod_iclk16,
        PulseWidthHigh => tpw_iclk16_posedge,
        PulseWidthLow => tpw_iclk16_negedge,
        PeriodData => periodcheckinfo_iclk16,
        Violation => tviol_iclk16_iclk16,
        MsgOn => MsgOn, XOn => XOn,
        HeaderMsg => InstancePath,
        CheckEnabled => TRUE,
        MsgSeverity => warning);

    END IF;

    PADDI_zd 	:= PADDI_out;

    VitalPathDelay01 (
      OutSignal => PADDI, OutSignalName => "PADDI", OutTemp => PADDI_zd,
      Paths      => (0 => (InputChangeTime => iclk16_ipd'last_event,
                           PathDelay => tpd_iclk16_PADDI,
                           PathCondition => TRUE)),
      GlitchData => PADDI_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity i_ft_clkB
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity i_ft_clkB is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "i_ft_clkB";

      tipd_iftclk  	: VitalDelayType01 := (0 ns, 0 ns);
      tpd_iftclk_PADDI	 : VitalDelayType01 := (0 ns, 0 ns);
      tperiod_iftclk 	: VitalDelayType := 0 ns;
      tpw_iftclk_posedge	: VitalDelayType := 0 ns;
      tpw_iftclk_negedge	: VitalDelayType := 0 ns);

    port (PADDI: out Std_logic; iftclk: in Std_logic);

    ATTRIBUTE Vital_Level0 OF i_ft_clkB : ENTITY IS TRUE;

  end i_ft_clkB;

  architecture Structure of i_ft_clkB is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDI_out 	: std_logic := 'X';
    signal iftclk_ipd 	: std_logic := 'X';

    component sapiobuf0002
      port (Z: out Std_logic; PAD: in Std_logic);
    end component;
  begin
    i_ft_clk_pad: sapiobuf0002
      port map (Z=>PADDI_out, PAD=>iftclk_ipd);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(iftclk_ipd, iftclk, tipd_iftclk);
    END BLOCK;

    VitalBehavior : PROCESS (PADDI_out, iftclk_ipd)
    VARIABLE PADDI_zd         	: std_logic := 'X';
    VARIABLE PADDI_GlitchData 	: VitalGlitchDataType;

    VARIABLE tviol_iftclk_iftclk          	: x01 := '0';
    VARIABLE periodcheckinfo_iftclk	: VitalPeriodDataType;

    BEGIN

    IF (TimingChecksOn) THEN
      VitalPeriodPulseCheck (
        TestSignal => iftclk_ipd,
        TestSignalName => "iftclk",
        Period => tperiod_iftclk,
        PulseWidthHigh => tpw_iftclk_posedge,
        PulseWidthLow => tpw_iftclk_negedge,
        PeriodData => periodcheckinfo_iftclk,
        Violation => tviol_iftclk_iftclk,
        MsgOn => MsgOn, XOn => XOn,
        HeaderMsg => InstancePath,
        CheckEnabled => TRUE,
        MsgSeverity => warning);

    END IF;

    PADDI_zd 	:= PADDI_out;

    VitalPathDelay01 (
      OutSignal => PADDI, OutSignalName => "PADDI", OutTemp => PADDI_zd,
      Paths      => (0 => (InputChangeTime => iftclk_ipd'last_event,
                           PathDelay => tpd_iftclk_PADDI,
                           PathCondition => TRUE)),
      GlitchData => PADDI_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity i_ft_be_1_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity i_ft_be_1_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "i_ft_be_1_B";

      tipd_iftbe1  	: VitalDelayType01 := (0 ns, 0 ns);
      tpd_iftbe1_PADDI	 : VitalDelayType01 := (0 ns, 0 ns);
      tperiod_iftbe1 	: VitalDelayType := 0 ns;
      tpw_iftbe1_posedge	: VitalDelayType := 0 ns;
      tpw_iftbe1_negedge	: VitalDelayType := 0 ns);

    port (PADDI: out Std_logic; iftbe1: in Std_logic);

    ATTRIBUTE Vital_Level0 OF i_ft_be_1_B : ENTITY IS TRUE;

  end i_ft_be_1_B;

  architecture Structure of i_ft_be_1_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDI_out 	: std_logic := 'X';
    signal iftbe1_ipd 	: std_logic := 'X';

    component sapiobuf0002
      port (Z: out Std_logic; PAD: in Std_logic);
    end component;
  begin
    i_ft_be_pad_1: sapiobuf0002
      port map (Z=>PADDI_out, PAD=>iftbe1_ipd);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(iftbe1_ipd, iftbe1, tipd_iftbe1);
    END BLOCK;

    VitalBehavior : PROCESS (PADDI_out, iftbe1_ipd)
    VARIABLE PADDI_zd         	: std_logic := 'X';
    VARIABLE PADDI_GlitchData 	: VitalGlitchDataType;

    VARIABLE tviol_iftbe1_iftbe1          	: x01 := '0';
    VARIABLE periodcheckinfo_iftbe1	: VitalPeriodDataType;

    BEGIN

    IF (TimingChecksOn) THEN
      VitalPeriodPulseCheck (
        TestSignal => iftbe1_ipd,
        TestSignalName => "iftbe1",
        Period => tperiod_iftbe1,
        PulseWidthHigh => tpw_iftbe1_posedge,
        PulseWidthLow => tpw_iftbe1_negedge,
        PeriodData => periodcheckinfo_iftbe1,
        Violation => tviol_iftbe1_iftbe1,
        MsgOn => MsgOn, XOn => XOn,
        HeaderMsg => InstancePath,
        CheckEnabled => TRUE,
        MsgSeverity => warning);

    END IF;

    PADDI_zd 	:= PADDI_out;

    VitalPathDelay01 (
      OutSignal => PADDI, OutSignalName => "PADDI", OutTemp => PADDI_zd,
      Paths      => (0 => (InputChangeTime => iftbe1_ipd'last_event,
                           PathDelay => tpd_iftbe1_PADDI,
                           PathCondition => TRUE)),
      GlitchData => PADDI_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity i_ft_be_0_B
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity i_ft_be_0_B is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "i_ft_be_0_B";

      tipd_iftbe0  	: VitalDelayType01 := (0 ns, 0 ns);
      tpd_iftbe0_PADDI	 : VitalDelayType01 := (0 ns, 0 ns);
      tperiod_iftbe0 	: VitalDelayType := 0 ns;
      tpw_iftbe0_posedge	: VitalDelayType := 0 ns;
      tpw_iftbe0_negedge	: VitalDelayType := 0 ns);

    port (PADDI: out Std_logic; iftbe0: in Std_logic);

    ATTRIBUTE Vital_Level0 OF i_ft_be_0_B : ENTITY IS TRUE;

  end i_ft_be_0_B;

  architecture Structure of i_ft_be_0_B is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDI_out 	: std_logic := 'X';
    signal iftbe0_ipd 	: std_logic := 'X';

    component sapiobuf0002
      port (Z: out Std_logic; PAD: in Std_logic);
    end component;
  begin
    i_ft_be_pad_0: sapiobuf0002
      port map (Z=>PADDI_out, PAD=>iftbe0_ipd);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(iftbe0_ipd, iftbe0, tipd_iftbe0);
    END BLOCK;

    VitalBehavior : PROCESS (PADDI_out, iftbe0_ipd)
    VARIABLE PADDI_zd         	: std_logic := 'X';
    VARIABLE PADDI_GlitchData 	: VitalGlitchDataType;

    VARIABLE tviol_iftbe0_iftbe0          	: x01 := '0';
    VARIABLE periodcheckinfo_iftbe0	: VitalPeriodDataType;

    BEGIN

    IF (TimingChecksOn) THEN
      VitalPeriodPulseCheck (
        TestSignal => iftbe0_ipd,
        TestSignalName => "iftbe0",
        Period => tperiod_iftbe0,
        PulseWidthHigh => tpw_iftbe0_posedge,
        PulseWidthLow => tpw_iftbe0_negedge,
        PeriodData => periodcheckinfo_iftbe0,
        Violation => tviol_iftbe0_iftbe0,
        MsgOn => MsgOn, XOn => XOn,
        HeaderMsg => InstancePath,
        CheckEnabled => TRUE,
        MsgSeverity => warning);

    END IF;

    PADDI_zd 	:= PADDI_out;

    VitalPathDelay01 (
      OutSignal => PADDI, OutSignalName => "PADDI", OutTemp => PADDI_zd,
      Paths      => (0 => (InputChangeTime => iftbe0_ipd'last_event,
                           PathDelay => tpd_iftbe0_PADDI,
                           PathCondition => TRUE)),
      GlitchData => PADDI_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity i_ft_txe_nB
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity i_ft_txe_nB is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "i_ft_txe_nB";

      tipd_ifttxen  	: VitalDelayType01 := (0 ns, 0 ns);
      tpd_ifttxen_PADDI	 : VitalDelayType01 := (0 ns, 0 ns);
      tperiod_ifttxen 	: VitalDelayType := 0 ns;
      tpw_ifttxen_posedge	: VitalDelayType := 0 ns;
      tpw_ifttxen_negedge	: VitalDelayType := 0 ns);

    port (PADDI: out Std_logic; ifttxen: in Std_logic);

    ATTRIBUTE Vital_Level0 OF i_ft_txe_nB : ENTITY IS TRUE;

  end i_ft_txe_nB;

  architecture Structure of i_ft_txe_nB is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDI_out 	: std_logic := 'X';
    signal ifttxen_ipd 	: std_logic := 'X';

    component sapiobuf0002
      port (Z: out Std_logic; PAD: in Std_logic);
    end component;
  begin
    i_ft_txe_n_pad: sapiobuf0002
      port map (Z=>PADDI_out, PAD=>ifttxen_ipd);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(ifttxen_ipd, ifttxen, tipd_ifttxen);
    END BLOCK;

    VitalBehavior : PROCESS (PADDI_out, ifttxen_ipd)
    VARIABLE PADDI_zd         	: std_logic := 'X';
    VARIABLE PADDI_GlitchData 	: VitalGlitchDataType;

    VARIABLE tviol_ifttxen_ifttxen          	: x01 := '0';
    VARIABLE periodcheckinfo_ifttxen	: VitalPeriodDataType;

    BEGIN

    IF (TimingChecksOn) THEN
      VitalPeriodPulseCheck (
        TestSignal => ifttxen_ipd,
        TestSignalName => "ifttxen",
        Period => tperiod_ifttxen,
        PulseWidthHigh => tpw_ifttxen_posedge,
        PulseWidthLow => tpw_ifttxen_negedge,
        PeriodData => periodcheckinfo_ifttxen,
        Violation => tviol_ifttxen_ifttxen,
        MsgOn => MsgOn, XOn => XOn,
        HeaderMsg => InstancePath,
        CheckEnabled => TRUE,
        MsgSeverity => warning);

    END IF;

    PADDI_zd 	:= PADDI_out;

    VitalPathDelay01 (
      OutSignal => PADDI, OutSignalName => "PADDI", OutTemp => PADDI_zd,
      Paths      => (0 => (InputChangeTime => ifttxen_ipd'last_event,
                           PathDelay => tpd_ifttxen_PADDI,
                           PathCondition => TRUE)),
      GlitchData => PADDI_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity i_ft_rxf_nB
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity i_ft_rxf_nB is
    -- miscellaneous vital GENERICs
    GENERIC (
      TimingChecksOn	: boolean := TRUE;
      XOn           	: boolean := FALSE;
      MsgOn         	: boolean := TRUE;
      InstancePath  	: string := "i_ft_rxf_nB";

      tipd_iftrxfn  	: VitalDelayType01 := (0 ns, 0 ns);
      tpd_iftrxfn_PADDI	 : VitalDelayType01 := (0 ns, 0 ns);
      tperiod_iftrxfn 	: VitalDelayType := 0 ns;
      tpw_iftrxfn_posedge	: VitalDelayType := 0 ns;
      tpw_iftrxfn_negedge	: VitalDelayType := 0 ns);

    port (PADDI: out Std_logic; iftrxfn: in Std_logic);

    ATTRIBUTE Vital_Level0 OF i_ft_rxf_nB : ENTITY IS TRUE;

  end i_ft_rxf_nB;

  architecture Structure of i_ft_rxf_nB is
    ATTRIBUTE Vital_Level0 OF Structure : ARCHITECTURE IS TRUE;

    signal PADDI_out 	: std_logic := 'X';
    signal iftrxfn_ipd 	: std_logic := 'X';

    component sapiobuf0002
      port (Z: out Std_logic; PAD: in Std_logic);
    end component;
  begin
    i_ft_rxf_n_pad: sapiobuf0002
      port map (Z=>PADDI_out, PAD=>iftrxfn_ipd);

    --  INPUT PATH DELAYs
    WireDelay : BLOCK
    BEGIN
      VitalWireDelay(iftrxfn_ipd, iftrxfn, tipd_iftrxfn);
    END BLOCK;

    VitalBehavior : PROCESS (PADDI_out, iftrxfn_ipd)
    VARIABLE PADDI_zd         	: std_logic := 'X';
    VARIABLE PADDI_GlitchData 	: VitalGlitchDataType;

    VARIABLE tviol_iftrxfn_iftrxfn          	: x01 := '0';
    VARIABLE periodcheckinfo_iftrxfn	: VitalPeriodDataType;

    BEGIN

    IF (TimingChecksOn) THEN
      VitalPeriodPulseCheck (
        TestSignal => iftrxfn_ipd,
        TestSignalName => "iftrxfn",
        Period => tperiod_iftrxfn,
        PulseWidthHigh => tpw_iftrxfn_posedge,
        PulseWidthLow => tpw_iftrxfn_negedge,
        PeriodData => periodcheckinfo_iftrxfn,
        Violation => tviol_iftrxfn_iftrxfn,
        MsgOn => MsgOn, XOn => XOn,
        HeaderMsg => InstancePath,
        CheckEnabled => TRUE,
        MsgSeverity => warning);

    END IF;

    PADDI_zd 	:= PADDI_out;

    VitalPathDelay01 (
      OutSignal => PADDI, OutSignalName => "PADDI", OutTemp => PADDI_zd,
      Paths      => (0 => (InputChangeTime => iftrxfn_ipd'last_event,
                           PathDelay => tpd_iftrxfn_PADDI,
                           PathCondition => TRUE)),
      GlitchData => PADDI_GlitchData,
      Mode       => vitaltransport, XOn => XOn, MsgOn => MsgOn);

    END PROCESS;

  end Structure;

-- entity kilsyth_top
  library IEEE, vital2000, ECP5U;
  use IEEE.STD_LOGIC_1164.all;
  use vital2000.vital_timing.all;
  use ECP5U.COMPONENTS.ALL;

  entity kilsyth_top is
    port (i_clk16: in Std_logic; 
          io_ft_data: out Std_logic_vector (15 downto 0); 
          i_ft_clk: in Std_logic; i_ft_be: in Std_logic_vector (1 downto 0); 
          i_ft_txe_n: in Std_logic; i_ft_rxf_n: in Std_logic; 
          o_ft_wr_n: out Std_logic; o_ft_rd_n: out Std_logic; 
          io_ft_oe_n: out Std_logic; io_ft_gpio1: in Std_logic; 
          o_leds: out Std_logic_vector (7 downto 0));



  end kilsyth_top;

  architecture Structure of kilsyth_top is
    signal n2: Std_logic;
    signal n3: Std_logic;
    signal n103: Std_logic;
    signal n104: Std_logic;
    signal i_clk16_c: Std_logic;
    signal n1041: Std_logic;
    signal n1042: Std_logic;
    signal n10_adj_1: Std_logic;
    signal n11: Std_logic;
    signal n111: Std_logic;
    signal n112: Std_logic;
    signal n1037: Std_logic;
    signal n1038: Std_logic;
    signal n12: Std_logic;
    signal n13: Std_logic;
    signal n113: Std_logic;
    signal n114: Std_logic;
    signal n1036: Std_logic;
    signal n14: Std_logic;
    signal n15: Std_logic;
    signal n115: Std_logic;
    signal n116: Std_logic;
    signal n1035: Std_logic;
    signal n16: Std_logic;
    signal n17: Std_logic;
    signal n117: Std_logic;
    signal n118: Std_logic;
    signal n1034: Std_logic;
    signal n18: Std_logic;
    signal n19: Std_logic;
    signal n119: Std_logic;
    signal n120: Std_logic;
    signal n1033: Std_logic;
    signal n20: Std_logic;
    signal n21: Std_logic;
    signal n121: Std_logic;
    signal n122: Std_logic;
    signal n1032: Std_logic;
    signal n22: Std_logic;
    signal n23: Std_logic;
    signal n123: Std_logic;
    signal n124: Std_logic;
    signal n1031: Std_logic;
    signal n24: Std_logic;
    signal n125: Std_logic;
    signal n4: Std_logic;
    signal n5: Std_logic;
    signal n105: Std_logic;
    signal n106: Std_logic;
    signal n1040: Std_logic;
    signal n6: Std_logic;
    signal n7: Std_logic;
    signal n107: Std_logic;
    signal n108: Std_logic;
    signal n1039: Std_logic;
    signal counter_23: Std_logic;
    signal n102: Std_logic;
    signal n8: Std_logic;
    signal n9: Std_logic;
    signal n109: Std_logic;
    signal n110: Std_logic;
    signal state_1: Std_logic;
    signal i_ft_clk_c_enable_3: Std_logic;
    signal i_ft_clk_c: Std_logic;
    signal ft_data_dir: Std_logic;
    signal state_0: Std_logic;
    signal n1122: Std_logic;
    signal i_ft_clk_c_enable_1: Std_logic;
    signal io_ft_oe_n_c: Std_logic;
    signal i_ft_txe_n_c: Std_logic;
    signal state_2: Std_logic;
    signal n1069: Std_logic;
    signal n1073: Std_logic;
    signal i_ft_clk_c_enable_6: Std_logic;
    signal next_state_0: Std_logic;
    signal next_state_1: Std_logic;
    signal n1067: Std_logic;
    signal i_ft_clk_c_enable_5: Std_logic;
    signal next_state_2: Std_logic;
    signal n1: Std_logic;
    signal i_ft_clk_c_enable_7: Std_logic;
    signal o_ft_rd_n_c: Std_logic;
    signal o_ft_wr_n_c: Std_logic;
    signal n1088: Std_logic;
    signal i_ft_be_c_0: Std_logic;
    signal o_leds_c_0: Std_logic;
    signal o_leds_c_1: Std_logic;
    signal i_ft_be_c_1: Std_logic;
    signal o_leds_c_2: Std_logic;
    signal o_leds_c_3: Std_logic;
    signal i_ft_rxf_n_c: Std_logic;
    signal o_leds_c_4: Std_logic;
    signal o_leds_c_5: Std_logic;
    signal o_leds_c_6: Std_logic;
    signal o_leds_6_N_2: Std_logic;
    signal n10: Std_logic;
    signal VCCI: Std_logic;
    component io_ft_data_15_B
      port (PADDT: in Std_logic; ioftdata15: out Std_logic);
    end component;
    component io_ft_data_14_B
      port (PADDT: in Std_logic; ioftdata14: out Std_logic);
    end component;
    component io_ft_data_13_B
      port (PADDT: in Std_logic; ioftdata13: out Std_logic);
    end component;
    component io_ft_data_12_B
      port (PADDT: in Std_logic; ioftdata12: out Std_logic);
    end component;
    component io_ft_data_11_B
      port (PADDT: in Std_logic; ioftdata11: out Std_logic);
    end component;
    component io_ft_data_10_B
      port (PADDT: in Std_logic; ioftdata10: out Std_logic);
    end component;
    component io_ft_data_9_B
      port (PADDT: in Std_logic; ioftdata9: out Std_logic);
    end component;
    component io_ft_data_8_B
      port (PADDT: in Std_logic; ioftdata8: out Std_logic);
    end component;
    component io_ft_data_7_B
      port (PADDT: in Std_logic; ioftdata7: out Std_logic);
    end component;
    component io_ft_data_6_B
      port (PADDT: in Std_logic; ioftdata6: out Std_logic);
    end component;
    component io_ft_data_5_B
      port (PADDT: in Std_logic; ioftdata5: out Std_logic);
    end component;
    component io_ft_data_4_B
      port (PADDT: in Std_logic; ioftdata4: out Std_logic);
    end component;
    component io_ft_data_3_B
      port (PADDT: in Std_logic; ioftdata3: out Std_logic);
    end component;
    component io_ft_data_2_B
      port (PADDT: in Std_logic; ioftdata2: out Std_logic);
    end component;
    component io_ft_data_1_B
      port (PADDT: in Std_logic; ioftdata1: out Std_logic);
    end component;
    component io_ft_data_0_B
      port (PADDT: in Std_logic; ioftdata0: out Std_logic);
    end component;
    component o_ft_wr_nB
      port (PADDO: in Std_logic; oftwrn: out Std_logic);
    end component;
    component o_ft_rd_nB
      port (PADDO: in Std_logic; oftrdn: out Std_logic);
    end component;
    component io_ft_oe_nB
      port (PADDO: in Std_logic; ioftoen: out Std_logic);
    end component;
    component o_leds_7_B
      port (oleds7: out Std_logic);
    end component;
    component o_leds_6_B
      port (PADDO: in Std_logic; oleds6: out Std_logic);
    end component;
    component o_leds_5_B
      port (PADDO: in Std_logic; oleds5: out Std_logic);
    end component;
    component o_leds_4_B
      port (PADDO: in Std_logic; oleds4: out Std_logic);
    end component;
    component o_leds_3_B
      port (PADDO: in Std_logic; oleds3: out Std_logic);
    end component;
    component o_leds_2_B
      port (PADDO: in Std_logic; oleds2: out Std_logic);
    end component;
    component o_leds_1_B
      port (PADDO: in Std_logic; oleds1: out Std_logic);
    end component;
    component o_leds_0_B
      port (PADDO: in Std_logic; oleds0: out Std_logic);
    end component;
    component i_clk16B
      port (PADDI: out Std_logic; iclk16: in Std_logic);
    end component;
    component i_ft_clkB
      port (PADDI: out Std_logic; iftclk: in Std_logic);
    end component;
    component i_ft_be_1_B
      port (PADDI: out Std_logic; iftbe1: in Std_logic);
    end component;
    component i_ft_be_0_B
      port (PADDI: out Std_logic; iftbe0: in Std_logic);
    end component;
    component i_ft_txe_nB
      port (PADDI: out Std_logic; ifttxen: in Std_logic);
    end component;
    component i_ft_rxf_nB
      port (PADDI: out Std_logic; iftrxfn: in Std_logic);
    end component;
  begin
    SLICE_0I: SCCU2C
      generic map (CLKMUX=>"SIG", CEMUX=>"VHI", CCU2_INJECT1_0=>"NO", 
                   CCU2_INJECT1_1=>"NO", GSR=>"DISABLED", SRMODE=>"ASYNC", 
                   INIT0_INITVAL=>X"CC00", INIT1_INITVAL=>X"AA00", 
                   REG1_SD=>"VHI", REG0_SD=>"VHI", CHECK_DI1=>TRUE, 
                   CHECK_DI0=>TRUE)
      port map (M1=>'X', A1=>n2, B1=>'X', C1=>'X', D1=>'1', DI1=>n103, 
                DI0=>n104, A0=>'X', B0=>n3, C0=>'X', D0=>'1', FCI=>n1041, 
                M0=>'X', CE=>'X', CLK=>i_clk16_c, LSR=>'X', FCO=>n1042, 
                F1=>n103, Q1=>n2, F0=>n104, Q0=>n3);
    SLICE_1I: SCCU2C
      generic map (CLKMUX=>"SIG", CEMUX=>"VHI", CCU2_INJECT1_0=>"NO", 
                   CCU2_INJECT1_1=>"NO", GSR=>"DISABLED", SRMODE=>"ASYNC", 
                   INIT0_INITVAL=>X"CC00", INIT1_INITVAL=>X"AA00", 
                   REG1_SD=>"VHI", REG0_SD=>"VHI", CHECK_DI1=>TRUE, 
                   CHECK_DI0=>TRUE)
      port map (M1=>'X', A1=>n10_adj_1, B1=>'X', C1=>'X', D1=>'1', DI1=>n111, 
                DI0=>n112, A0=>'X', B0=>n11, C0=>'X', D0=>'1', FCI=>n1037, 
                M0=>'X', CE=>'X', CLK=>i_clk16_c, LSR=>'X', FCO=>n1038, 
                F1=>n111, Q1=>n10_adj_1, F0=>n112, Q0=>n11);
    SLICE_2I: SCCU2C
      generic map (CLKMUX=>"SIG", CEMUX=>"VHI", CCU2_INJECT1_0=>"NO", 
                   CCU2_INJECT1_1=>"NO", GSR=>"DISABLED", SRMODE=>"ASYNC", 
                   INIT0_INITVAL=>X"CC00", INIT1_INITVAL=>X"AA00", 
                   REG1_SD=>"VHI", REG0_SD=>"VHI", CHECK_DI1=>TRUE, 
                   CHECK_DI0=>TRUE)
      port map (M1=>'X', A1=>n12, B1=>'X', C1=>'X', D1=>'1', DI1=>n113, 
                DI0=>n114, A0=>'X', B0=>n13, C0=>'X', D0=>'1', FCI=>n1036, 
                M0=>'X', CE=>'X', CLK=>i_clk16_c, LSR=>'X', FCO=>n1037, 
                F1=>n113, Q1=>n12, F0=>n114, Q0=>n13);
    SLICE_3I: SCCU2C
      generic map (CLKMUX=>"SIG", CEMUX=>"VHI", CCU2_INJECT1_0=>"NO", 
                   CCU2_INJECT1_1=>"NO", GSR=>"DISABLED", SRMODE=>"ASYNC", 
                   INIT0_INITVAL=>X"CC00", INIT1_INITVAL=>X"CC00", 
                   REG1_SD=>"VHI", REG0_SD=>"VHI", CHECK_DI1=>TRUE, 
                   CHECK_DI0=>TRUE)
      port map (M1=>'X', A1=>'X', B1=>n14, C1=>'X', D1=>'1', DI1=>n115, 
                DI0=>n116, A0=>'X', B0=>n15, C0=>'X', D0=>'1', FCI=>n1035, 
                M0=>'X', CE=>'X', CLK=>i_clk16_c, LSR=>'X', FCO=>n1036, 
                F1=>n115, Q1=>n14, F0=>n116, Q0=>n15);
    SLICE_4I: SCCU2C
      generic map (CLKMUX=>"SIG", CEMUX=>"VHI", CCU2_INJECT1_0=>"NO", 
                   CCU2_INJECT1_1=>"NO", GSR=>"DISABLED", SRMODE=>"ASYNC", 
                   INIT0_INITVAL=>X"CC00", INIT1_INITVAL=>X"CC00", 
                   REG1_SD=>"VHI", REG0_SD=>"VHI", CHECK_DI1=>TRUE, 
                   CHECK_DI0=>TRUE)
      port map (M1=>'X', A1=>'X', B1=>n16, C1=>'X', D1=>'1', DI1=>n117, 
                DI0=>n118, A0=>'X', B0=>n17, C0=>'X', D0=>'1', FCI=>n1034, 
                M0=>'X', CE=>'X', CLK=>i_clk16_c, LSR=>'X', FCO=>n1035, 
                F1=>n117, Q1=>n16, F0=>n118, Q0=>n17);
    SLICE_5I: SCCU2C
      generic map (CLKMUX=>"SIG", CEMUX=>"VHI", CCU2_INJECT1_0=>"NO", 
                   CCU2_INJECT1_1=>"NO", GSR=>"DISABLED", SRMODE=>"ASYNC", 
                   INIT0_INITVAL=>X"CC00", INIT1_INITVAL=>X"AA00", 
                   REG1_SD=>"VHI", REG0_SD=>"VHI", CHECK_DI1=>TRUE, 
                   CHECK_DI0=>TRUE)
      port map (M1=>'X', A1=>n18, B1=>'X', C1=>'X', D1=>'1', DI1=>n119, 
                DI0=>n120, A0=>'X', B0=>n19, C0=>'X', D0=>'1', FCI=>n1033, 
                M0=>'X', CE=>'X', CLK=>i_clk16_c, LSR=>'X', FCO=>n1034, 
                F1=>n119, Q1=>n18, F0=>n120, Q0=>n19);
    SLICE_6I: SCCU2C
      generic map (CLKMUX=>"SIG", CEMUX=>"VHI", CCU2_INJECT1_0=>"NO", 
                   CCU2_INJECT1_1=>"NO", GSR=>"DISABLED", SRMODE=>"ASYNC", 
                   INIT0_INITVAL=>X"CC00", INIT1_INITVAL=>X"AA00", 
                   REG1_SD=>"VHI", REG0_SD=>"VHI", CHECK_DI1=>TRUE, 
                   CHECK_DI0=>TRUE)
      port map (M1=>'X', A1=>n20, B1=>'X', C1=>'X', D1=>'1', DI1=>n121, 
                DI0=>n122, A0=>'X', B0=>n21, C0=>'X', D0=>'1', FCI=>n1032, 
                M0=>'X', CE=>'X', CLK=>i_clk16_c, LSR=>'X', FCO=>n1033, 
                F1=>n121, Q1=>n20, F0=>n122, Q0=>n21);
    SLICE_7I: SCCU2C
      generic map (CLKMUX=>"SIG", CEMUX=>"VHI", CCU2_INJECT1_0=>"NO", 
                   CCU2_INJECT1_1=>"NO", GSR=>"DISABLED", SRMODE=>"ASYNC", 
                   INIT0_INITVAL=>X"CC00", INIT1_INITVAL=>X"CC00", 
                   REG1_SD=>"VHI", REG0_SD=>"VHI", CHECK_DI1=>TRUE, 
                   CHECK_DI0=>TRUE)
      port map (M1=>'X', A1=>'X', B1=>n22, C1=>'X', D1=>'1', DI1=>n123, 
                DI0=>n124, A0=>'X', B0=>n23, C0=>'X', D0=>'1', FCI=>n1031, 
                M0=>'X', CE=>'X', CLK=>i_clk16_c, LSR=>'X', FCO=>n1032, 
                F1=>n123, Q1=>n22, F0=>n124, Q0=>n23);
    SLICE_8I: SCCU2C
      generic map (CLKMUX=>"SIG", CEMUX=>"VHI", CCU2_INJECT1_0=>"NO", 
                   CCU2_INJECT1_1=>"NO", GSR=>"DISABLED", SRMODE=>"ASYNC", 
                   INIT0_INITVAL=>X"0000", INIT1_INITVAL=>X"33FF", 
                   REG1_SD=>"VHI", CHECK_DI1=>TRUE)
      port map (M1=>'X', A1=>'X', B1=>n24, C1=>'X', D1=>'1', DI1=>n125, 
                DI0=>'X', A0=>'X', B0=>'X', C0=>'X', D0=>'X', FCI=>'X', 
                M0=>'X', CE=>'X', CLK=>i_clk16_c, LSR=>'X', FCO=>n1031, 
                F1=>n125, Q1=>n24, F0=>open, Q0=>open);
    SLICE_9I: SCCU2C
      generic map (CLKMUX=>"SIG", CEMUX=>"VHI", CCU2_INJECT1_0=>"NO", 
                   CCU2_INJECT1_1=>"NO", GSR=>"DISABLED", SRMODE=>"ASYNC", 
                   INIT0_INITVAL=>X"CC00", INIT1_INITVAL=>X"AA00", 
                   REG1_SD=>"VHI", REG0_SD=>"VHI", CHECK_DI1=>TRUE, 
                   CHECK_DI0=>TRUE)
      port map (M1=>'X', A1=>n4, B1=>'X', C1=>'X', D1=>'1', DI1=>n105, 
                DI0=>n106, A0=>'X', B0=>n5, C0=>'X', D0=>'1', FCI=>n1040, 
                M0=>'X', CE=>'X', CLK=>i_clk16_c, LSR=>'X', FCO=>n1041, 
                F1=>n105, Q1=>n4, F0=>n106, Q0=>n5);
    SLICE_10I: SCCU2C
      generic map (CLKMUX=>"SIG", CEMUX=>"VHI", CCU2_INJECT1_0=>"NO", 
                   CCU2_INJECT1_1=>"NO", GSR=>"DISABLED", SRMODE=>"ASYNC", 
                   INIT0_INITVAL=>X"CC00", INIT1_INITVAL=>X"CC00", 
                   REG1_SD=>"VHI", REG0_SD=>"VHI", CHECK_DI1=>TRUE, 
                   CHECK_DI0=>TRUE)
      port map (M1=>'X', A1=>'X', B1=>n6, C1=>'X', D1=>'1', DI1=>n107, 
                DI0=>n108, A0=>'X', B0=>n7, C0=>'X', D0=>'1', FCI=>n1039, 
                M0=>'X', CE=>'X', CLK=>i_clk16_c, LSR=>'X', FCO=>n1040, 
                F1=>n107, Q1=>n6, F0=>n108, Q0=>n7);
    SLICE_11I: SCCU2C
      generic map (CLKMUX=>"SIG", CEMUX=>"VHI", CCU2_INJECT1_0=>"NO", 
                   CCU2_INJECT1_1=>"NO", GSR=>"DISABLED", SRMODE=>"ASYNC", 
                   INIT0_INITVAL=>X"CC00", INIT1_INITVAL=>X"0000", 
                   REG0_SD=>"VHI", CHECK_DI0=>TRUE)
      port map (M1=>'X', A1=>'X', B1=>'X', C1=>'X', D1=>'X', DI1=>'X', 
                DI0=>n102, A0=>'X', B0=>counter_23, C0=>'X', D0=>'1', 
                FCI=>n1042, M0=>'X', CE=>'X', CLK=>i_clk16_c, LSR=>'X', 
                FCO=>open, F1=>open, Q1=>open, F0=>n102, Q0=>counter_23);
    SLICE_12I: SCCU2C
      generic map (CLKMUX=>"SIG", CEMUX=>"VHI", CCU2_INJECT1_0=>"NO", 
                   CCU2_INJECT1_1=>"NO", GSR=>"DISABLED", SRMODE=>"ASYNC", 
                   INIT0_INITVAL=>X"CC00", INIT1_INITVAL=>X"CC00", 
                   REG1_SD=>"VHI", REG0_SD=>"VHI", CHECK_DI1=>TRUE, 
                   CHECK_DI0=>TRUE)
      port map (M1=>'X', A1=>'X', B1=>n8, C1=>'X', D1=>'1', DI1=>n109, 
                DI0=>n110, A0=>'X', B0=>n9, C0=>'X', D0=>'1', FCI=>n1038, 
                M0=>'X', CE=>'X', CLK=>i_clk16_c, LSR=>'X', FCO=>n1039, 
                F1=>n109, Q1=>n8, F0=>n110, Q0=>n9);
    SLICE_13I: SLOGICB
      generic map (M0MUX=>"SIG", CLKMUX=>"SIG", CEMUX=>"SIG", GSR=>"DISABLED", 
                   SRMODE=>"ASYNC", CHECK_M0=>TRUE, CHECK_CE=>TRUE)
      port map (M1=>'X', FXA=>'X', FXB=>'X', A1=>'X', B1=>'X', C1=>'X', 
                D1=>'X', DI1=>'X', DI0=>'X', A0=>'X', B0=>'X', C0=>'X', 
                D0=>'X', M0=>state_1, CE=>i_ft_clk_c_enable_3, CLK=>i_ft_clk_c, 
                LSR=>'X', OFX1=>open, F1=>open, Q1=>open, OFX0=>open, F0=>open, 
                Q0=>ft_data_dir);
    SLICE_14I: SLOGICB
      generic map (CLKMUX=>"SIG", CEMUX=>"SIG", REG0_REGSET=>"SET", 
                   GSR=>"DISABLED", SRMODE=>"ASYNC", LUT0_INITVAL=>X"0505", 
                   REG0_SD=>"VHI", CHECK_DI0=>TRUE, CHECK_CE=>TRUE)
      port map (M1=>'X', FXA=>'X', FXB=>'X', A1=>'X', B1=>'X', C1=>'X', 
                D1=>'X', DI1=>'X', DI0=>n1122, A0=>state_1, B0=>'X', 
                C0=>state_0, D0=>'X', M0=>'X', CE=>i_ft_clk_c_enable_1, 
                CLK=>i_ft_clk_c, LSR=>'X', OFX1=>open, F1=>open, Q1=>open, 
                OFX0=>open, F0=>n1122, Q0=>io_ft_oe_n_c);
    SLICE_15I: SLOGICB
      generic map (CLKMUX=>"SIG", CEMUX=>"SIG", GSR=>"DISABLED", 
                   SRMODE=>"ASYNC", LUT0_INITVAL=>X"0111", 
                   LUT1_INITVAL=>X"4444", REG1_SD=>"VHI", REG0_SD=>"VHI", 
                   CHECK_DI1=>TRUE, CHECK_DI0=>TRUE, CHECK_CE=>TRUE)
      port map (M1=>'X', FXA=>'X', FXB=>'X', A1=>state_1, B1=>state_0, C1=>'X', 
                D1=>'X', DI1=>n1069, DI0=>n1073, A0=>state_1, B0=>state_0, 
                C0=>state_2, D0=>i_ft_txe_n_c, M0=>'X', 
                CE=>i_ft_clk_c_enable_6, CLK=>i_ft_clk_c, LSR=>'X', OFX1=>open, 
                F1=>n1069, Q1=>next_state_1, OFX0=>open, F0=>n1073, 
                Q0=>next_state_0);
    SLICE_16I: SLOGICB
      generic map (CLKMUX=>"SIG", CEMUX=>"SIG", GSR=>"DISABLED", 
                   SRMODE=>"ASYNC", LUT0_INITVAL=>X"CC00", REG0_SD=>"VHI", 
                   CHECK_DI0=>TRUE, CHECK_CE=>TRUE)
      port map (M1=>'X', FXA=>'X', FXB=>'X', A1=>'X', B1=>'X', C1=>'X', 
                D1=>'X', DI1=>'X', DI0=>n1067, A0=>'X', B0=>state_1, C0=>'X', 
                D0=>state_0, M0=>'X', CE=>i_ft_clk_c_enable_5, CLK=>i_ft_clk_c, 
                LSR=>'X', OFX1=>open, F1=>open, Q1=>open, OFX0=>open, 
                F0=>n1067, Q0=>next_state_2);
    SLICE_17I: SLOGICB
      generic map (CLKMUX=>"SIG", CEMUX=>"SIG", REG0_REGSET=>"SET", 
                   GSR=>"DISABLED", SRMODE=>"ASYNC", LUT0_INITVAL=>X"00FF", 
                   REG0_SD=>"VHI", CHECK_DI0=>TRUE, CHECK_CE=>TRUE)
      port map (M1=>'X', FXA=>'X', FXB=>'X', A1=>'X', B1=>'X', C1=>'X', 
                D1=>'X', DI1=>'X', DI0=>n1, A0=>'X', B0=>'X', C0=>'X', 
                D0=>state_0, M0=>'X', CE=>i_ft_clk_c_enable_7, CLK=>i_ft_clk_c, 
                LSR=>'X', OFX1=>open, F1=>open, Q1=>open, OFX0=>open, F0=>n1, 
                Q0=>o_ft_rd_n_c);
    SLICE_18I: SLOGICB
      generic map (CLKMUX=>"SIG", CEMUX=>"INV", REG0_REGSET=>"SET", 
                   GSR=>"DISABLED", SRMODE=>"ASYNC", LUT0_INITVAL=>X"30F3", 
                   REG0_SD=>"VHI", CHECK_DI0=>TRUE, CHECK_CE=>TRUE)
      port map (M1=>'X', FXA=>'X', FXB=>'X', A1=>'X', B1=>'X', C1=>'X', 
                D1=>'X', DI1=>'X', DI0=>n1088, A0=>'X', B0=>state_1, 
                C0=>o_ft_wr_n_c, D0=>state_0, M0=>'X', CE=>state_2, 
                CLK=>i_ft_clk_c, LSR=>'X', OFX1=>open, F1=>open, Q1=>open, 
                OFX0=>open, F0=>n1088, Q0=>o_ft_wr_n_c);
    SLICE_19I: SLOGICB
      generic map (M0MUX=>"SIG", M1MUX=>"SIG", CLKMUX=>"SIG", CEMUX=>"VHI", 
                   GSR=>"DISABLED", SRMODE=>"ASYNC", CHECK_M1=>TRUE, 
                   CHECK_M0=>TRUE)
      port map (M1=>i_ft_be_c_0, FXA=>'X', FXB=>'X', A1=>'X', B1=>'X', C1=>'X', 
                D1=>'X', DI1=>'X', DI0=>'X', A0=>'X', B0=>'X', C0=>'X', 
                D0=>'X', M0=>counter_23, CE=>'X', CLK=>i_clk16_c, LSR=>'X', 
                OFX1=>open, F1=>open, Q1=>o_leds_c_1, OFX0=>open, F0=>open, 
                Q0=>o_leds_c_0);
    SLICE_20I: SLOGICB
      generic map (M0MUX=>"SIG", M1MUX=>"SIG", CLKMUX=>"SIG", CEMUX=>"VHI", 
                   GSR=>"DISABLED", SRMODE=>"ASYNC", CHECK_M1=>TRUE, 
                   CHECK_M0=>TRUE)
      port map (M1=>i_ft_txe_n_c, FXA=>'X', FXB=>'X', A1=>'X', B1=>'X', 
                C1=>'X', D1=>'X', DI1=>'X', DI0=>'X', A0=>'X', B0=>'X', 
                C0=>'X', D0=>'X', M0=>i_ft_be_c_1, CE=>'X', CLK=>i_clk16_c, 
                LSR=>'X', OFX1=>open, F1=>open, Q1=>o_leds_c_3, OFX0=>open, 
                F0=>open, Q0=>o_leds_c_2);
    SLICE_21I: SLOGICB
      generic map (M0MUX=>"SIG", M1MUX=>"SIG", CLKMUX=>"SIG", CEMUX=>"VHI", 
                   GSR=>"DISABLED", SRMODE=>"ASYNC", CHECK_M1=>TRUE, 
                   CHECK_M0=>TRUE)
      port map (M1=>o_ft_rd_n_c, FXA=>'X', FXB=>'X', A1=>'X', B1=>'X', C1=>'X', 
                D1=>'X', DI1=>'X', DI0=>'X', A0=>'X', B0=>'X', C0=>'X', 
                D0=>'X', M0=>i_ft_rxf_n_c, CE=>'X', CLK=>i_clk16_c, LSR=>'X', 
                OFX1=>open, F1=>open, Q1=>o_leds_c_5, OFX0=>open, F0=>open, 
                Q0=>o_leds_c_4);
    SLICE_22I: SLOGICB
      generic map (CLKMUX=>"SIG", CEMUX=>"VHI", GSR=>"DISABLED", 
                   SRMODE=>"ASYNC", LUT0_INITVAL=>X"00FF", REG0_SD=>"VHI", 
                   CHECK_DI0=>TRUE)
      port map (M1=>'X', FXA=>'X', FXB=>'X', A1=>'X', B1=>'X', C1=>'X', 
                D1=>'X', DI1=>'X', DI0=>o_leds_6_N_2, A0=>'X', B0=>'X', 
                C0=>'X', D0=>o_leds_c_6, M0=>'X', CE=>'X', CLK=>i_ft_clk_c, 
                LSR=>'X', OFX1=>open, F1=>open, Q1=>open, OFX0=>open, 
                F0=>o_leds_6_N_2, Q0=>o_leds_c_6);
    SLICE_23I: SLOGICB
      generic map (M0MUX=>"SIG", M1MUX=>"SIG", CLKMUX=>"SIG", CEMUX=>"VHI", 
                   GSR=>"DISABLED", SRMODE=>"ASYNC", CHECK_M1=>TRUE, 
                   CHECK_M0=>TRUE)
      port map (M1=>next_state_1, FXA=>'X', FXB=>'X', A1=>'X', B1=>'X', 
                C1=>'X', D1=>'X', DI1=>'X', DI0=>'X', A0=>'X', B0=>'X', 
                C0=>'X', D0=>'X', M0=>next_state_0, CE=>'X', CLK=>i_ft_clk_c, 
                LSR=>'X', OFX1=>open, F1=>open, Q1=>state_1, OFX0=>open, 
                F0=>open, Q0=>state_0);
    i426_SLICE_25I: SLOGICB
      generic map (M0MUX=>"SIG", LUT0_INITVAL=>X"008B", LUT1_INITVAL=>X"3333")
      port map (M1=>'X', FXA=>'X', FXB=>'X', A1=>'X', B1=>state_2, C1=>'X', 
                D1=>'X', DI1=>'X', DI0=>'X', A0=>i_ft_txe_n_c, B0=>state_2, 
                C0=>i_ft_rxf_n_c, D0=>state_1, M0=>state_0, CE=>'X', CLK=>'X', 
                LSR=>'X', OFX1=>open, F1=>open, Q1=>open, 
                OFX0=>i_ft_clk_c_enable_5, F0=>open, Q0=>open);
    SLICE_26I: SLOGICB
      generic map (LUT0_INITVAL=>X"0C55", LUT1_INITVAL=>X"5D0C")
      port map (M1=>'X', FXA=>'X', FXB=>'X', A1=>state_1, B1=>state_0, 
                C1=>state_2, D1=>n10, DI1=>'X', DI0=>'X', A0=>i_ft_rxf_n_c, 
                B0=>i_ft_txe_n_c, C0=>state_0, D0=>state_2, M0=>'X', CE=>'X', 
                CLK=>'X', LSR=>'X', OFX1=>open, F1=>i_ft_clk_c_enable_6, 
                Q1=>open, OFX0=>open, F0=>n10, Q0=>open);
    SLICE_27I: SLOGICB
      generic map (LUT0_INITVAL=>X"0F03")
      port map (M1=>'X', FXA=>'X', FXB=>'X', A1=>'X', B1=>'X', C1=>'X', 
                D1=>'X', DI1=>'X', DI0=>'X', A0=>'X', B0=>state_1, C0=>state_2, 
                D0=>state_0, M0=>'X', CE=>'X', CLK=>'X', LSR=>'X', OFX1=>open, 
                F1=>open, Q1=>open, OFX0=>open, F0=>i_ft_clk_c_enable_1, 
                Q0=>open);
    SLICE_28I: SLOGICB
      generic map (LUT0_INITVAL=>X"00F0")
      port map (M1=>'X', FXA=>'X', FXB=>'X', A1=>'X', B1=>'X', C1=>'X', 
                D1=>'X', DI1=>'X', DI0=>'X', A0=>'X', B0=>'X', C0=>state_0, 
                D0=>state_2, M0=>'X', CE=>'X', CLK=>'X', LSR=>'X', OFX1=>open, 
                F1=>open, Q1=>open, OFX0=>open, F0=>i_ft_clk_c_enable_3, 
                Q0=>open);
    SLICE_29I: SLOGICB
      generic map (M0MUX=>"SIG", CLKMUX=>"SIG", CEMUX=>"VHI", GSR=>"DISABLED", 
                   SRMODE=>"ASYNC", LUT0_INITVAL=>X"000F", CHECK_M0=>TRUE)
      port map (M1=>'X', FXA=>'X', FXB=>'X', A1=>'X', B1=>'X', C1=>'X', 
                D1=>'X', DI1=>'X', DI0=>'X', A0=>'X', B0=>'X', C0=>state_2, 
                D0=>state_1, M0=>next_state_2, CE=>'X', CLK=>i_ft_clk_c, 
                LSR=>'X', OFX1=>open, F1=>open, Q1=>open, OFX0=>open, 
                F0=>i_ft_clk_c_enable_7, Q0=>state_2);
    io_ft_data_15_I: io_ft_data_15_B
      port map (PADDT=>ft_data_dir, ioftdata15=>io_ft_data(15));
    io_ft_data_14_I: io_ft_data_14_B
      port map (PADDT=>ft_data_dir, ioftdata14=>io_ft_data(14));
    io_ft_data_13_I: io_ft_data_13_B
      port map (PADDT=>ft_data_dir, ioftdata13=>io_ft_data(13));
    io_ft_data_12_I: io_ft_data_12_B
      port map (PADDT=>ft_data_dir, ioftdata12=>io_ft_data(12));
    io_ft_data_11_I: io_ft_data_11_B
      port map (PADDT=>ft_data_dir, ioftdata11=>io_ft_data(11));
    io_ft_data_10_I: io_ft_data_10_B
      port map (PADDT=>ft_data_dir, ioftdata10=>io_ft_data(10));
    io_ft_data_9_I: io_ft_data_9_B
      port map (PADDT=>ft_data_dir, ioftdata9=>io_ft_data(9));
    io_ft_data_8_I: io_ft_data_8_B
      port map (PADDT=>ft_data_dir, ioftdata8=>io_ft_data(8));
    io_ft_data_7_I: io_ft_data_7_B
      port map (PADDT=>ft_data_dir, ioftdata7=>io_ft_data(7));
    io_ft_data_6_I: io_ft_data_6_B
      port map (PADDT=>ft_data_dir, ioftdata6=>io_ft_data(6));
    io_ft_data_5_I: io_ft_data_5_B
      port map (PADDT=>ft_data_dir, ioftdata5=>io_ft_data(5));
    io_ft_data_4_I: io_ft_data_4_B
      port map (PADDT=>ft_data_dir, ioftdata4=>io_ft_data(4));
    io_ft_data_3_I: io_ft_data_3_B
      port map (PADDT=>ft_data_dir, ioftdata3=>io_ft_data(3));
    io_ft_data_2_I: io_ft_data_2_B
      port map (PADDT=>ft_data_dir, ioftdata2=>io_ft_data(2));
    io_ft_data_1_I: io_ft_data_1_B
      port map (PADDT=>ft_data_dir, ioftdata1=>io_ft_data(1));
    io_ft_data_0_I: io_ft_data_0_B
      port map (PADDT=>ft_data_dir, ioftdata0=>io_ft_data(0));
    o_ft_wr_nI: o_ft_wr_nB
      port map (PADDO=>o_ft_wr_n_c, oftwrn=>o_ft_wr_n);
    o_ft_rd_nI: o_ft_rd_nB
      port map (PADDO=>o_ft_rd_n_c, oftrdn=>o_ft_rd_n);
    io_ft_oe_nI: io_ft_oe_nB
      port map (PADDO=>io_ft_oe_n_c, ioftoen=>io_ft_oe_n);
    o_leds_7_I: o_leds_7_B
      port map (oleds7=>o_leds(7));
    o_leds_6_I: o_leds_6_B
      port map (PADDO=>o_leds_c_6, oleds6=>o_leds(6));
    o_leds_5_I: o_leds_5_B
      port map (PADDO=>o_leds_c_5, oleds5=>o_leds(5));
    o_leds_4_I: o_leds_4_B
      port map (PADDO=>o_leds_c_4, oleds4=>o_leds(4));
    o_leds_3_I: o_leds_3_B
      port map (PADDO=>o_leds_c_3, oleds3=>o_leds(3));
    o_leds_2_I: o_leds_2_B
      port map (PADDO=>o_leds_c_2, oleds2=>o_leds(2));
    o_leds_1_I: o_leds_1_B
      port map (PADDO=>o_leds_c_1, oleds1=>o_leds(1));
    o_leds_0_I: o_leds_0_B
      port map (PADDO=>o_leds_c_0, oleds0=>o_leds(0));
    i_clk16I: i_clk16B
      port map (PADDI=>i_clk16_c, iclk16=>i_clk16);
    i_ft_clkI: i_ft_clkB
      port map (PADDI=>i_ft_clk_c, iftclk=>i_ft_clk);
    i_ft_be_1_I: i_ft_be_1_B
      port map (PADDI=>i_ft_be_c_1, iftbe1=>i_ft_be(1));
    i_ft_be_0_I: i_ft_be_0_B
      port map (PADDI=>i_ft_be_c_0, iftbe0=>i_ft_be(0));
    i_ft_txe_nI: i_ft_txe_nB
      port map (PADDI=>i_ft_txe_n_c, ifttxen=>i_ft_txe_n);
    i_ft_rxf_nI: i_ft_rxf_nB
      port map (PADDI=>i_ft_rxf_n_c, iftrxfn=>i_ft_rxf_n);
    VHI_INST: VHI
      port map (Z=>VCCI);
    PUR_INST: PUR
      port map (PUR=>VCCI);
    GSR_INST: GSR
      port map (GSR=>VCCI);
  end Structure;



  library IEEE, vital2000, ECP5U;
  configuration Structure_CON of kilsyth_top is
    for Structure
    end for;
  end Structure_CON;


