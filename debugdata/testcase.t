repo @System 0 testtags @System.repo.gz
repo pgdg94 -99.-1000 testtags pgdg94.repo.gz
repo rpmfusion-nonfree -99.-1000 testtags rpmfusion-nonfree.repo.gz
repo rommon-telegram -99.-1000 testtags rommon-telegram.repo.gz
repo slacktechnologies_slack-source -99.-1000 testtags slacktechnologies_slack-source.repo.gz
repo mysql57-community -99.-1000 testtags mysql57-community.repo.gz
repo mail.ru-cloud -99.-1000 testtags mail.ru-cloud.repo.gz
repo rpmfusion-nonfree-updates -99.-1000 testtags rpmfusion-nonfree-updates.repo.gz
repo updates -99.-1000 testtags updates.repo.gz
repo adobe-linux-x86_64 -99.-1000 testtags adobe-linux-x86_64.repo.gz
repo rpmfusion-free-updates -99.-1000 testtags rpmfusion-free-updates.repo.gz
repo slacktechnologies_slack -99.-1000 testtags slacktechnologies_slack.repo.gz
repo google-chrome -99.-1000 testtags google-chrome.repo.gz
repo Dropbox -99.-1000 testtags Dropbox.repo.gz
repo rpmfusion-free -99.-1000 testtags rpmfusion-free.repo.gz
repo mysql-connectors-community -99.-1000 testtags mysql-connectors-community.repo.gz
repo fedora -99.-1000 testtags fedora.repo.gz
repo mysql-tools-community -99.-1000 testtags mysql-tools-community.repo.gz
system x86_64 rpm @System
poolflags implicitobsoleteusescolors
disable pkg postgresql-9.5.5-1.fc24.x86_64@updates
disable pkg postgresql-contrib-9.5.5-1.fc24.x86_64@updates
disable pkg postgresql-devel-9.5.5-1.fc24.i686@updates
disable pkg postgresql-devel-9.5.5-1.fc24.x86_64@updates
disable pkg postgresql-docs-9.5.5-1.fc24.x86_64@updates
disable pkg postgresql-libs-9.5.5-1.fc24.i686@updates
disable pkg postgresql-libs-9.5.5-1.fc24.x86_64@updates
disable pkg postgresql-plperl-9.5.5-1.fc24.x86_64@updates
disable pkg postgresql-plpython-9.5.5-1.fc24.x86_64@updates
disable pkg postgresql-plpython3-9.5.5-1.fc24.x86_64@updates
disable pkg postgresql-pltcl-9.5.5-1.fc24.x86_64@updates
disable pkg postgresql-server-9.5.5-1.fc24.x86_64@updates
disable pkg postgresql-static-9.5.5-1.fc24.i686@updates
disable pkg postgresql-static-9.5.5-1.fc24.x86_64@updates
disable pkg postgresql-test-9.5.5-1.fc24.x86_64@updates
disable pkg postgresql-upgrade-9.5.5-1.fc24.x86_64@updates
disable pkg postgresql-9.5.3-1.fc24.x86_64@fedora
disable pkg postgresql-contrib-9.5.3-1.fc24.x86_64@fedora
disable pkg postgresql-dbi-link-2.0.0-13.fc24.noarch@fedora
disable pkg postgresql-devel-9.5.3-1.fc24.i686@fedora
disable pkg postgresql-devel-9.5.3-1.fc24.x86_64@fedora
disable pkg postgresql-docs-9.5.3-1.fc24.x86_64@fedora
disable pkg postgresql-ip4r-2.0.2-9.fc24.x86_64@fedora
disable pkg postgresql-jdbc-9.4.1200-3.fc24.noarch@fedora
disable pkg postgresql-jdbc-javadoc-9.4.1200-3.fc24.noarch@fedora
disable pkg postgresql-libs-9.5.3-1.fc24.i686@fedora
disable pkg postgresql-libs-9.5.3-1.fc24.x86_64@fedora
disable pkg postgresql-odbc-09.05.0100-2.fc24.x86_64@fedora
disable pkg postgresql-odbc-tests-09.05.0100-2.fc24.x86_64@fedora
disable pkg postgresql-pgpool-II-3.5.2-1.fc24.i686@fedora
disable pkg postgresql-pgpool-II-3.5.2-1.fc24.x86_64@fedora
disable pkg postgresql-pgpool-II-devel-3.5.2-1.fc24.i686@fedora
disable pkg postgresql-pgpool-II-devel-3.5.2-1.fc24.x86_64@fedora
disable pkg postgresql-pgpool-II-extensions-3.5.2-1.fc24.x86_64@fedora
disable pkg postgresql-pgpoolAdmin-3.4.0-3.fc24.noarch@fedora
disable pkg postgresql-plperl-9.5.3-1.fc24.x86_64@fedora
disable pkg postgresql-plpython-9.5.3-1.fc24.x86_64@fedora
disable pkg postgresql-plpython3-9.5.3-1.fc24.x86_64@fedora
disable pkg postgresql-plruby-0.5.4-9.fc24.x86_64@fedora
disable pkg postgresql-plruby-doc-0.5.4-9.fc24.x86_64@fedora
disable pkg postgresql-pltcl-9.5.3-1.fc24.x86_64@fedora
disable pkg postgresql-server-9.5.3-1.fc24.x86_64@fedora
disable pkg postgresql-static-9.5.3-1.fc24.i686@fedora
disable pkg postgresql-static-9.5.3-1.fc24.x86_64@fedora
disable pkg postgresql-test-9.5.3-1.fc24.x86_64@fedora
disable pkg postgresql-upgrade-9.5.3-1.fc24.x86_64@fedora
disable pkg postgresql_autodoc-1.41-6.fc24.noarch@fedora
solverflags allowvendorchange keepexplicitobsoletes bestobeypolicy keeporphans yumobsoletes
job update name vim-minimal
job multiversion provides kernel
job multiversion provides installonlypkg(kernel)
job multiversion provides installonlypkg(kernel-module)
job multiversion provides installonlypkg(vm)
result transaction,problems solver.result
