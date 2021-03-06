"""
    {"publisher": "",
     "publisher_keys": [],
     "name": "",
     "version": "",
     "url": "",
     "gpg_signature": "",
     "gpg_signature_url": "",
     "sha1": "",
     "sha256": "",
     "sha512": "",
     },
"""
RELEASES = [
    # GnuPG
    {"publisher": "GnuPG",
     "publisher_keys": [
         "D8692123C4065DEA5E0F3AB5249B39D24F25E3B6",
         "46CC730865BB5C78EBABADCF04376F3EE0856959",
         "031EC2536E580D8EA286A9F22071B08A33BD3F06",
         "D238EA65D64C67ED4C3073F28A861B1C7EFD60D9",
     ],
     "name": "GNU Privacy Guard",
     "version": "2.2.1",
     "url": "https://gnupg.org/ftp/gcrypt/gnupg/gnupg-2.2.1.tar.bz2",
     "gpg_signature": "",
     "gpg_signature_url": "https://gnupg.org/ftp/gcrypt/gnupg/gnupg-2.2.1.tar.bz2.sig",
     "sha1": "5455373fd7208b787f319027de2464721cdd4413",
     "sha256": "34d70cd65b9c95f3f2f90a9f5c1e0b6a0fe039a8d685e2d66d69c33d1cbf62fb",
     },

    # Tails
    {"publisher": "Tails",
     "publisher_keys": ["A490D0F4D311A4153E2BB7CADBB802B258ACD84F"],
     "name": "Tails",
     "version": "3.2",
     "url": "https://mirrors.ocf.berkeley.edu/tails/stable/tails-amd64-3.2/tails-amd64-3.2.iso",
     "gpg_signature": "",
     "gpg_signature_url": "https://tails.boum.org/torrents/files/tails-amd64-3.2.iso.sig",
     "sha1": "5ff7fb7a69fad712e00837eeb5e61be546d1026d",
     "sha256": "6ead2c7ce076458a31082f1f27444ea94542fe8ee007665e927dfb93c9232a01",
     },

    # Tor
    {"publisher": "Tor Project",
     "publisher_keys": ["EF6E286DDA85EA2A4BA7DE684E2C6E8793298290"],
     "name": "Tor Browser Windows",
     "version": "7.0.6",
     "url": "https://www.torproject.org/dist/torbrowser/7.0.6/torbrowser-install-7.0.6_en-US.exe",
     "gpg_signature": "",
     "gpg_signature_url": "https://www.torproject.org/dist/torbrowser/7.0.6/torbrowser-install-7.0.6_en-US.exe.asc",
     "sha1": "2ce89a307bc3288ee70c0c45b9dba0d4d49b16ab",
     "sha256": "af1b26a2d74b890284e9a2b7826a43bd96d3fe34ba2e54f6b384f3fb226797c8",
     },
    {"publisher": "Tor Project",
     "publisher_keys": ["EF6E286DDA85EA2A4BA7DE684E2C6E8793298290"],
     "name": "Tor Browser OS X",
     "version": "7.0.6",
     "url": "https://www.torproject.org/dist/torbrowser/7.0.6/TorBrowser-7.0.6-osx64_en-US.dmg",
     "gpg_signature": "",
     "gpg_signature_url": "https://www.torproject.org/dist/torbrowser/7.0.6/TorBrowser-7.0.6-osx64_en-US.dmg.asc",
     "sha1": "66f73f7c17b4d2932e425bfc6bafa36956e50ed7",
     "sha256": "4a5b638d2ecc4d7dc4a8708d7d14a1456674ace74a453dc08dc3f3dd4ef47dfb",
     },
    {"publisher": "Tor Project",
     "publisher_keys": ["EF6E286DDA85EA2A4BA7DE684E2C6E8793298290"],
     "name": "Tor Browser Linux",
     "version": "7.0.6",
     "url": "https://www.torproject.org/dist/torbrowser/7.0.6/tor-browser-linux64-7.0.6_en-US.tar.xz",
     "gpg_signature": "",
     "gpg_signature_url": "https://www.torproject.org/dist/torbrowser/7.0.6/tor-browser-linux64-7.0.6_en-US.tar.xz.asc",
     "sha1": "df0eb090e6e5aa274a9694f0dbee9d1a42b072a7",
     "sha256": "d5e0b7803902d08868bae59de3f939d390c513cc944c9aa28be8dc730ac8e387",
     },

    # Veracrypt
    {"publisher": "IDRIX",
     "publisher_keys": ["993B7D7E8E413809828F0F29EB559C7C54DDD393"],
     "name": "Veracrypt",
     "version": "1.21",
     "url": "https://launchpad.net/veracrypt/trunk/1.21/+download/VeraCrypt_1.21_Bundle.7z",
     "gpg_signature": "",
     "gpg_signature_url": "https://launchpad.net/veracrypt/trunk/1.21/+download/VeraCrypt_1.21_Bundle.7z.sig",
     "sha1": "e92dff966cde096894a4011c4d179eb4226ef908",
     "sha256": "8a6458adb8d50a06af134b4eab7f135bc306f51a691e4eccb70b314e8a04e09d",
     },

    # OS X Fuse

    # Whonix

    # Yubikey
    {"publisher": "Yubico",
     "publisher_keys": ["20EE325B86A81BCBD3E56798F04367096FBA95E8"],
     "name": "YubiKey NEO Manager Linux",
     "version": "1.4.0",
     "url": "https://developers.yubico.com/yubikey-neo-manager/Releases/yubikey-neo-manager-1.4.0.tar.gz",
     "gpg_signature": "",
     "gpg_signature_url": "https://developers.yubico.com/yubikey-neo-manager/Releases/yubikey-neo-manager-1.4.0.tar.gz.sig",
     "sha1": "152196386b327072fc29315b84f3fb7bf2680c72",
     "sha256": "2fb8fc72982a8158379d2ac46802d26eb288bed09e33fe78df0a4c7844df5dc7",
     },
    {"publisher": "Yubico",
     "publisher_keys": ["20EE325B86A81BCBD3E56798F04367096FBA95E8"],
     "name": "YubiKey NEO Manager OS X",
     "version": "1.4.0",
     "url": "https://developers.yubico.com/yubikey-neo-manager/Releases/yubikey-neo-manager-1.4.0-mac.pkg",
     "gpg_signature": "",
     "gpg_signature_url": "https://developers.yubico.com/yubikey-neo-manager/Releases/yubikey-neo-manager-1.4.0-mac.pkg.sig",
     "sha1": "1ef53a34012272e0057ecb0737b9678aa55b051a",
     "sha256": "b1af0f922bb8b6da285bf34bc012f48773c2529b4e128fe9a48f4ef768f70bd4",
     },
    {"publisher": "Yubico",
     "publisher_keys": ["20EE325B86A81BCBD3E56798F04367096FBA95E8"],
     "name": "YubiKey NEO Manager Windows",
     "version": "1.4.0",
     "url": "https://developers.yubico.com/yubikey-neo-manager/Releases/yubikey-neo-manager-1.4.0-win.exe",
     "gpg_signature": "",
     "gpg_signature_url": "https://developers.yubico.com/yubikey-neo-manager/Releases/yubikey-neo-manager-1.4.0-win.exe.sig",
     "sha1": "ef03f0a6c30d137aec66e9ff4b6eaba4153f083b",
     "sha256": "d7d03379af80ae15487106c685dceacf1851d6d4d59bde29117c42b9b83167e2",
     },

    # GPG4Win
    {"publisher": "Gpg4win",
     "publisher_keys": [
         "61AC3F5EE4BE593C13D68B1E7CBD620BEC70B1B8",
         "13E3CE81AFEA6F683E466E0D42D876082688DA1A",
     ],
     "name": "Gpg4win",
     "version": "3.0.0",
     "url": "https://files.gpg4win.org/gpg4win-3.0.0.exe",
     "gpg_signature": "",
     "gpg_signature_url": "https://files.gpg4win.org/gpg4win-3.0.0.exe.sig",
     "sha1": "8262d1818b4f9a890ce6182cafdb9510387e88e0",
     "sha256": "2565bf6faf8defb8fa61b0b1a30f0e68e2ca5ceb3177d08516e00ca1620252bf",
     },
    {"publisher": "Gpg4win",
     "publisher_keys": [],
     "name": "Gpg4win Source",
     "version": "3.0.0",
     "url": "https://files.gpg4win.org/gpg4win-3.0.0.tar.bz2",
     "gpg_signature": "",
     "gpg_signature_url": "https://files.gpg4win.org/gpg4win-3.0.0.tar.bz2.sig",
     "sha1": "2dc412675632da44c7f4dc120f1b2e866e350573",
     "sha256": "120cd3e8826d6e3e9f35b86b59973e8d1dd7ce713a42c20fe9493f720cf3569c",
     },

    # GPG Tools
    {"publisher": "GPG Tools",
     "publisher_keys": ["85E38F69046B44C1EC9FB07B76D78F0500D026C4"],
     "name": "GPG Suite",
     "version": "2017.1",
     "url": "https://releases.gpgtools.org/GPG_Suite-2017.1.dmg",
     "gpg_signature": "",
     "gpg_signature_url": "https://releases.gpgtools.org/GPG_Suite-2017.1.dmg.sig",
     "sha1": "d5a05565d0e9782236ea06455e555fafe0f32fc2",
     "sha256": "01705da33b9dadaf5282d28f9ef58f2eb7cd8ff6f19b4ade78861bf87668a061",
     },
    {"publisher": "GPG Tools",
     "publisher_keys": ["85E38F69046B44C1EC9FB07B76D78F0500D026C4"],
     "name": "GPG Suite Source",
     "version": "2017.1",
     "url": "https://releases.gpgtools.org/GPG_Suite-2017.1.txz",
     "gpg_signature": "",
     "gpg_signature_url": "https://releases.gpgtools.org/GPG_Suite-2017.1.txz.sig",
     "sha1": "49e4558cb28d6a5b932764996eeaabf9427cb409",
     "sha256": "f625931d878075c1d931478446ea1168e51041cf7c32a575ff9bf2a1033ae605",
     },

    # OpenSSL
    {"publisher": "OpenSSL",
     "publisher_keys": ["8657ABB260F056B1E5190839D9C4D26D0E604491"],
     "name": "OpenSSL",
     "version": "1.1.0f",
     "url": "https://www.openssl.org/source/openssl-1.1.0f.tar.gz",
     "gpg_signature": "",
     "gpg_signature_url": "https://www.openssl.org/source/openssl-1.1.0f.tar.gz.asc",
     "sha1": "9e3e02bc8b4965477a7a1d33be1249299a9deb15",
     "sha256": "12f746f3f2493b2f39da7ecf63d7ee19c6ac9ec6a4fcd8c229da8a522cb12765",
     },

    # LibreSSL
    {"publisher": "LibreSSL",
     "publisher_keys": ["A1EB079B8D3EB92B4EBD3139663AF51BD5E4D8D5"],
     "name": "LibreSSL",
     "version": "2.5.5",
     "url": "https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/libressl-2.5.5.tar.gz",
     "gpg_signature": "",
     "gpg_signature_url": "https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/libressl-2.5.5.tar.gz.asc",
     "sha1": "36511c98fe450bbb50da8c8a3d4eba2cc7d0f83c",
     "sha256": "e57f5e3d5842a81fe9351b6e817fcaf0a749ca4ef35a91465edba9e071dce7c4",
     },
    {"publisher": "LibreSSL",
     "publisher_keys": ["A1EB079B8D3EB92B4EBD3139663AF51BD5E4D8D5"],
     "name": "LibreSSL Windows",
     "version": "2.5.5",
     "url": "https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/libressl-2.5.5-windows.zip",
     "gpg_signature": "",
     "gpg_signature_url": "",
     "sha1": "c825ae3df24abfc04545c0a5269884d3faeeb1bb",
     "sha256": "21edeba00eab78a5af8302bf5543bade4da53d584edc4e56d67dbb91edf2a56c",
     },

    # OpenSSH
    {"publisher": "OpenSSH",
     "publisher_keys": ["59C2118ED206D927E667EBE3D3E5F56B6D920D30"],
     "name": "OpenSSH",
     "version": "7.5",
     "url": "https://ftp.openbsd.org/pub/OpenBSD/OpenSSH/openssh-7.5.tar.gz",
     "gpg_signature": "",
     "gpg_signature_url": "https://ftp.openbsd.org/pub/OpenBSD/OpenSSH/openssh-7.5.tar.gz.asc",
     "sha1": "81384df377e38551f7659a4c250383d0bbd25341",
     "sha256": "1a693c8ce74674a6bb362c5437927e6d331f7ae9b9571f0dbfe95e01d40dab75",
     },

    # OpenVPN
    {"publisher": "OpenVPN",
     "publisher_keys": ["6D04F8F1B0173111F499795E29584D9F40864578"],
     "name": "OpenVPN Source",
     "version": "2.4.3",
     "url": "https://swupdate.openvpn.org/community/releases/openvpn-2.4.3.tar.gz",
     "gpg_signature": "",
     "gpg_signature_url": "https://swupdate.openvpn.org/community/releases/openvpn-2.4.3.tar.gz.asc",
     "sha1": "0630f30858ff2199739246f1295871226e0a7705",
     "sha256": "cee3d3ca462960a50a67c0ebd186e01b6d13db70275205663695152c9aca8579",
     },
    {"publisher": "OpenVPN",
     "publisher_keys": ["6D04F8F1B0173111F499795E29584D9F40864578"],
     "name": "OpenVPN Windows",
     "version": "2.4.3",
     "url": "https://swupdate.openvpn.org/community/releases/openvpn-install-2.4.3-I602.exe",
     "gpg_signature": "",
     "gpg_signature_url": "https://swupdate.openvpn.org/community/releases/openvpn-install-2.4.3-I602.exe.asc",
     "sha1": "a839cadba139a5761884b567a82546ec9a2e9b0b",
     "sha256": "f722ff1d187951c4e7454e2d845ba6d0d43d505112e073fa60b67b350fd6bc87",
     },

    # Tunnelblick
    {"publisher": "Tunnelblick",
     "publisher_keys": [],
     "name": "Tunnelblick",
     "version": "3.7.2",
     "url": "https://www.tunnelblick.net/release/Tunnelblick_3.7.2_build_4850.dmg",
     "gpg_signature": "",
     "gpg_signature_url": "",
     "sha1": "2fb79ed21f54036deeb5df470aeab16ea85406d8",
     "sha256": "1a56e4335023de54985f68731b9ca114d0a2aa08124623642f2e8b200e67726d",
     },
]
