
SRCBRANCH = "2018.03"
SRC_URI = "git://github.com/PGSEnergy/u-boot.git;branch=${SRCBRANCH} \
           "
SRCREV = "fce8edb4ee61a1e383e528406bb45d5a0c7c0173"


addtask copy_defconfig_vf after do_unpack before do_preconfigure

do_copy_defconfig_vf () {
	install -d ${B}
	mkdir -p ${B}
	cp ${S}/arch/arm/configs/ea_imx_defconfig ${B}/.config
        cp ${S}/arch/arm/configs/ea_imx_defconfig ${B}/../defconfig
}
