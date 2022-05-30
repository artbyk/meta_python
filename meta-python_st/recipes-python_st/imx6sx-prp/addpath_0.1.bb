SUMMARY = "Add prp stack to file system"
SECTION = "PRP"
LICENSE = "CLOSED"

SRC_URI = "file://profile"

S = "${WORKDIR}"


do_install() {
		install -d 777 ${D}/etc
		install -m 777 profile ${D}/etc/
}

FILES_${PN} += "/etc"
