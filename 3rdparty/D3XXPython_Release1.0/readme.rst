FTD3XX


Description
    ftd3xx is a simple Python wrapper library around FTDI's `D3XX DLL` using ctypes.
    It allows customers to write Python-based applications in Windows or Linux to communicate with FT600/FT601 devices.
    Demo applications (APIUsage, DataLoopback, DataStreamer, ChipConfig) are provided to jumpstart development with FT60X.
    Aside from Python language, note that FTDI provides D3XX libraries for C/C++ and C# (.NET) languages.
    For more information, refer to the following websites:
        http://www.ftdichip.com/Drivers/D3XX.htm 
        http://www.ftdichip.com/Support/SoftwareExamples/FT60X.htm
        http://www.ftdichip.com/Products/ICs/FT600.html

API List
    listDevices
    createDeviceInfoList
    getDeviceInfoList
    getDeviceInfoDetail
    create
    getStrError
    raiseExceptionOnError
    FTD3XX
        close
		getLastError
        writePipe
        readPipe - caller provides the buffer (faster performance)
        readPipeEx - function allocates the buffer (easier concatenation)
        flushPipe
        getDeviceInfo
        getDeviceDescriptor
        getStringDescriptor
        getConfigurationDescriptor
        getInterfaceDescriptor
        getPipeInformation
        getChipConfiguration
        setChipConfiguration
        getVIDPID
        getLibraryVersion
        getDriverVersion
        getFirmwareVersion
        resetDevicePort
        enableGPIO
        writeGPIO
        readGPIO
        setGPIOPull
    Windows only
        FTD3XX
            setPipeTimeout
            getPipeTimeout
            setStreamPipe
            clearStreamPipe
            abortPipe
            cycleDevicePort
            setSuspendTimeout
            getSuspendTimeout
     Linux only
        setTransferParams
        FTD3XX
            getReadQueueStatus
            getWriteQueueStatus
            getUnsentBuffer
			
Package
    ftd3xx\
        __init__.py
        _ftd3xx.py
        defines.py
        ftd3xx.py
        demo\
            apiusage.py 
            dataloopback.py 
            datastreaming.py 
    readme.rst
    setup.py
    ftd3xx.dll (not present in the package - download latest from ftdi web)
        Windows D3XX user library
		Go to FTDI website to ensure to get the latest version
        Copy the appropriate driver .DLL file based on the OS architecture (32-bit or 64 bit)
    libftd3xx.so (not present in the package - download latest from ftdi web)
        Linux D3XX user library
        Go to FTDI website to ensure to get the latest version
        Copy the appropriate driver .SO file based on the OS architecture (32-bit or 64 bit)

Requirements
    Windows
        D3XX driver	
            Download and install D3XX driver automatically from Windows Update by plugging in FT60x device
            Then go to FTDI website to ensure to get the latest driver version
            http://www.ftdichip.com/Drivers/D3XX.htm
        Python 2.7.12
            Download and install Python 2.7.12 from
   	        https://www.python.org/downloads/release/python-2712/ 
            Note: Download 64-bit if using 64-bit machine to avoid "... is not a valid Windows application" error
    Linux
        D3XX driver	
            Download and install D3XX driver from
            http://www.ftdichip.com/Drivers/D3XX.htm
        Python 2.7.12
            Download and install Python 2.7.12
            python --version
            sudo apt-get install build-essential checkinstall
            sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
            cd /usr/src
            wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz
            sudo tar xzf Python-2.7.12.tgz
            cd Python-2.7.12
            sudo ./configure
            sudo make altinstall
            python --version
        pip and setuptools
            Download and install pip which contains setuptools
            sudo apt-get install python-pip		
            export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.7/dist-packages
            sudo chmod 777 /usr/local/lib/python2.7/site-packages/
			
Library Compilation
    Windows
        ftd3xx\ftd3xx.py
            Produces defines.py and ftd3xx_win32.pyc
        ftd3xx\__init__.py
            Produces ftd3xx.pyc
    Linux
        ftd3xx/ftd3xx.py
            Produces defines.py and ftd3xx_linux.pyc
        ftd3xx/__init__.py
            Produces ftd3xx.pyc
    
Library Installation
    setup.py install
	
Demo Execution
    ftd3xx\demo\apiusage.py
    ftd3xx\demo\dataloopback.py
    ftd3xx\demo\datastreaming.py
    ftd3xx\demo\chipconfiguration.py

Known Limitations of Python Wrapper Implementations
    Asynchronus transfer not supported
    Notifications feature not supported
    Refer to Windows D3XX driver and Linux D3XX driver for other limitations and issues


