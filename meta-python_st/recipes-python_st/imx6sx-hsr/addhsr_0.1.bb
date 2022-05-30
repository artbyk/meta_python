SUMMARY = "Add HSR python script to file system"
SECTION = "HSR"
LICENSE = "CLOSED"

SRC_URI = "file://HSR.py \
		   file://ksz8463.py \
		   file://mac.txt"

S = "${WORKDIR}"


do_install() {
	     install -d 777 ${D}/kepm/hsr
	     install -m 777 HSR.py ${D}/kepm/hsr/
		 install -m 777 ksz8463.py ${D}/kepm/hsr/
		 install -m 777 mac.txt ${D}/kepm/hsr/
}

FILES_${PN} += "/kepm/hsr"