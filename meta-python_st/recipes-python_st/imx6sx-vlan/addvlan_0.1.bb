SUMMARY = "Add prp stack to file system"
SECTION = "PRP"
LICENSE = "CLOSED"

SRC_URI = "file://vlan.py"

S = "${WORKDIR}"


do_install() {
	     install -d 777 ${D}/kepm/vlan
		 install -m 777 vlan.py ${D}/kepm/vlan/
}

FILES_${PN} += "/kepm/vlan"
