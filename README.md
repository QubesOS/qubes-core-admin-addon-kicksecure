qubes-core-admin extension for handling Kicksecure related settings
-------------------------------------------------------------------

This extension takes care of setting up Kicksecure VMs. When a new VM is
created based on a template with `kicksecure` feature set, it gets a tag
`sdwdate-gui-client` used for sdwdate-gui qrexec functions.

Additionally, Kicksecure template can request `kicksecure` feature to be added
to itself, easing bootstrap of this feature. The canonical way to do this, is
to place a script in `/etc/qubes/post-install.d` (with `.sh` extension), with
just one call:

    qvm-features-request kicksecure 1

This will set the `kicksecure` feature, and also add the `sdwdate-gui-client`
tag. The template cannot request the feature to be removed.
