#!/bin/bash

# locate libreoffice snap package
LO_SNAP_PACKAGE=$(mount | grep libreoffice_REPLACEREV | cut -d " " -f 1)
LO_SNAP_MOUNTPOINT="REPLACEMOUNTPOINT"
LO_SNAP_NAME=$(echo $LO_SNAP_PACKAGE | cut -d "/" -f 6)
LO_USER_DIR="REPLACEUSERDIR"
LO_INTRO_PATH="REPLACEINTRO"
LO_SOFFICERC_PATH="REPLACESOFFICERC"
LO_PERSONAS_PATH="REPLACEPERSONAS"

if [[ "$LO_USER_DIR" == *"REPLACE"* || "$LO_INTRO_PATH" == *"REPLACE"* || "$LO_SOFFICERC_PATH" == *"REPLACE"* || "$LO_PERSONAS_PATH" == *"REPLACE"* ]]; then
    echo "Oops, you need to run extension from libreoffice first. Exiting ..."
    exit 1
fi

echo "LibreOffice snap location: $LO_SNAP_PACKAGE"
echo "LibreOffice mount point: $LO_SNAP_MOUNTPOINT"

# unmount LO first
echo "Unmounting libreoffice ..."
sudo umount $LO_SNAP_PACKAGE

sleep 1

# copy original snap for uninstall
echo "Backing up snap packge to $HOME/.local/share/$LO_SNAP_NAME ..."
sudo cp -v $LO_SNAP_PACKAGE $HOME/.local/share/

sleep 1

# unsquashfs the snap package
echo "Extracting Libreoffice snap package to squashfs-root ..."
sudo unsquashfs $LO_SNAP_PACKAGE

# modify the snap package
pushd squashfs-root/lib/libreoffice
echo "Preparing snap ..."
# setup intro.png
sudo mv program/intro.png program/intro.png.orig
sudo ln -s "$LO_INTRO_PATH" program/intro.png
echo "[Done] intro.png"
sleep 1
# setup sofficerc
sudo mv program/sofficerc program/sofficerc.orig
sudo ln -s "$LO_SOFFICERC_PATH" program/sofficerc
echo "[Done] sofficerc"
sleep 1

# setup personas dir
sudo mv share/gallery/personas share/gallery/personas.orig
sudo ln -s "$LO_PERSONAS_PATH" share/gallery/personas
echo "[Done] personas dir"
popd

sleep 1

# repack into snap package
echo "Now repacking snap package ..."
sudo mksquashfs squashfs-root $LO_SNAP_NAME
echo "[Done] Preparing new LibreOffice snap"
sleep 1

# copy back to snap directory
echo "Copying new LibreOffice snap to $LO_SNAP_PACKAGE ..."
sudo cp -v $LO_SNAP_NAME $LO_SNAP_PACKAGE

sleep 1

# remount snap package
echo "Mounting new LibreOffice snap to $LO_SNAP_MOUNTPOINT ..."
sudo mount -t squashfs -o ro,nodev,relatime,x-gdu.hide $LO_SNAP_PACKAGE $LO_SNAP_MOUNTPOINT

sleep 1

# removing squashfs-root folder
echo "Cleaning up ..."
sudo rm -rf squashfs-root $LO_SNAP_NAME
echo "finished" > "$LO_USER_DIR"/lotc-prepare

sleep 1

echo "[Success] Snap preparation for LO-TC-GUI"
echo "Now, you can change theme from LibreOffice Extension menu"
