SUMMARY = "Add prp stack to file system"
SECTION = "PRP"
LICENSE = "CLOSED"

SRC_URI = "file://sw_stack_prp1-master/prp_pcap_tap_userspace/prp_stack \
		   file://sw_stack_prp1-master/prp_pcap_tap_userspace/prp_conf.txt \
		   file://prpstart.sh \
		   file://prp.py \
		   file://prpstop.sh"

S = "${WORKDIR}"


do_install() {
	     install -d 777 ${D}/kepm/prp
		#  cp -r ${WORKDIR}/sw_stack_prp1-master/prp_pcap_tap_userspace/prp_pcap_tap_userspace ${D}/kepm/prp/
		 install -m 777 ${WORKDIR}/sw_stack_prp1-master/prp_pcap_tap_userspace/prp_stack ${D}/kepm/prp/
		 install -m 777 ${WORKDIR}/sw_stack_prp1-master/prp_pcap_tap_userspace/prp_conf.txt ${D}/kepm/prp/
		 install -m 777 prpstart.sh ${D}/kepm/prp/
		 install -m 777 prpstop.sh ${D}/kepm/prp/
		 install -m 777 prp.py ${D}/kepm/prp/
}

FILES_${PN} += "/kepm/prp"
