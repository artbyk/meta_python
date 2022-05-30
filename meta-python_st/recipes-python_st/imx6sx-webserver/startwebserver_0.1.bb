SUMMARY = "Add webserver python for autostartup"
SECTION = "SCRIPTS"
LICENSE = "CLOSED"

SRC_URI = "file://webserver.service"
inherit systemd
SYSTEMD_SERVICE_${PN} = "webserver.service"

S = "${WORKDIR}"
INITSCRIPT_NAME = "webserver.service"

do_install() {
             install -d ${D}${systemd_unitdir}/system
             install -m 0644 ${WORKDIR}/${INITSCRIPT_NAME} ${D}${systemd_unitdir}/system
}