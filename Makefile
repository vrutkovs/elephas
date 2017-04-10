FLATPAK ?= flatpak --user

all: install-deps build prune install-repo
	$(FLATPAK) update com.github.Elephas

install-deps:
	$(FLATPAK) --user remote-add --if-not-exists --from gnome-nightly https://sdk.gnome.org/gnome.flatpakrepo
	$(FLATPAK) --user install gnome-nightly org.gnome.Platform/x86_64/master org.gnome.Sdk/x86_64/master || true

build:
	flatpak-builder --force-clean --ccache --repo=repo \
		--subject="Nightly build of Elephas, `date`" \
		${EXPORT_ARGS} app com.github.Elephas.json

prune:
	flatpak build-update-repo --prune --prune-depth=20 repo || true

install-repo:
	$(FLATPAK) remote-add --if-not-exists --no-gpg-verify nightly-elephas ./repo
	$(FLATPAK) -v install nightly-elephas com.github.Elephas || true
