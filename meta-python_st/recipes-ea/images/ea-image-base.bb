SUMMARY = "A small image just capable of allowing a device to boot."

IMAGE_INSTALL = "\
   packagegroup-core-boot ${CORE_IMAGE_EXTRA_INSTALL} \
   ea-files \
"

GLIBC_GENERATE_LOCALES = "en_GB.UTF-8 en_US.UTF-8"
IMAGE_LINGUAS ?= "en-gb"

LICENSE = "MIT"

inherit core-image

IMAGE_ROOTFS_SIZE ?= "8192"
IMAGE_ROOTFS_EXTRA_SPACE_append = "${@bb.utils.contains("DISTRO_FEATURES", "systemd", " + 4096", "" ,d)}"
