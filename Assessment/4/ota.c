

if (new_version_available()) {
    download_firmware();
    if (verify_signature() && verify_hash()) {
        install_new_firmware();
        reboot();
    } else {
        keep_old_firmware();
    }
}
