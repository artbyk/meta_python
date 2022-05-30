SUMMARY = "Add ksz8463 python script to file system"
SECTION = "KSZ"
LICENSE = "CLOSED"

SRC_URI = "file://ksz8463.py \
	   file://sel_copp_fib.py "

S = "${WORKDIR}"


do_install() {
	     install -d 777 ${D}/kepm/ksz
	     install -m 777 ksz8463.py ${D}/kepm/ksz/
		 install -m 777 sel_copp_fib.py ${D}/kepm/ksz/
}

FILES_${PN} += "/kepm/ksz"
