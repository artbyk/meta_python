SUMMARY = "Add web server to file system"
SECTION = "Web"
LICENSE = "CLOSED"

SRC_URI = "file://Flask_orion"

S = "${WORKDIR}"


do_install() {
	     install -d 777 ${D}/kepm/web
		 cp -r ${WORKDIR}/Flask_orion ${D}/kepm/web/
		 
}

FILES_${PN} += "/kepm/web"
