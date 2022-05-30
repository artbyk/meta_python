SUMMARY = "Add ksz8463 python script to file system"
SECTION = "KSZ"
LICENSE = "CLOSED"

SRC_URI = "file://ksz8463.py \
		   file://sel_copp_fib.py "

S = "${WORKDIR}"


do_install() {
	     install -d 777 ${D}/ksz
	     install -m 777 ksz8463.py ${D}/ksz/
		 install -m 777 sel_copp_fib.py ${D}/ksz/
}

FILES_${PN} += "/ksz"
