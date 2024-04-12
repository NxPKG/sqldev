# Release Notes

## Latest Changes

### Docs

* 📝 Update ModelRead to ModelPublic documentation and examples. PR [#885](https://github.com/khulnasoft/sqldev/pull/885) by [@estebanx64](https://github.com/estebanx64).
* ✨ Add source examples for Python 3.10 and 3.9 with updated syntax. PR [#842](https://github.com/khulnasoft/sqldev/pull/842) by [@khulnasoft](https://github.com/khulnasoft) and [@estebanx64](https://github.com/estebanx64).

### Internal

* 🔧 Update MkDocs, disable cards while I can upgrade to the latest MkDocs Material, that fixes an issue with social cards. PR [#888](https://github.com/khulnasoft/sqldev/pull/888) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Add cron to run test once a week on monday. PR [#869](https://github.com/khulnasoft/sqldev/pull/869) by [@estebanx64](https://github.com/estebanx64).
* ⬆️ Upgrade Ruff version and configs. PR [#859](https://github.com/khulnasoft/sqldev/pull/859) by [@khulnasoft](https://github.com/khulnasoft).
* 🔥 Remove Jina QA Bot as it has been discontinued. PR [#840](https://github.com/khulnasoft/sqldev/pull/840) by [@khulnasoft](https://github.com/khulnasoft).

## 0.0.16

### Features

* ✨ Add new method `.sqldev_update()` to update models in place, including an `update` parameter for extra data. And fix implementation for the (now documented) `update` parameter for `.model_validate()`. PR [#804](https://github.com/khulnasoft/sqldev/pull/804) by [@khulnasoft](https://github.com/khulnasoft).
    * Updated docs: [Update Data with FastAPI](https://sqldev.khulnasoft.com/tutorial/fastapi/update/).
    * New docs: [Update with Extra Data (Hashed Passwords) with FastAPI](https://sqldev.khulnasoft.com/tutorial/fastapi/update-extra-data/).

## 0.0.15

### Fixes

* 🐛 Fix class initialization compatibility with Pydantic and SQLDev, fixing errors revealed by the latest Pydantic. PR [#807](https://github.com/khulnasoft/sqldev/pull/807) by [@khulnasoft](https://github.com/khulnasoft).

### Internal

* ⬆ Bump khulnasoft/issue-manager from 0.4.0 to 0.4.1. PR [#775](https://github.com/khulnasoft/sqldev/pull/775) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Fix GitHub Actions build docs filter paths for GitHub workflows. PR [#738](https://github.com/khulnasoft/sqldev/pull/738) by [@khulnasoft](https://github.com/khulnasoft).

## 0.0.14

### Features

* ✨ Add support for Pydantic v2 (while keeping support for v1 if v2 is not available). PR [#722](https://github.com/khulnasoft/sqldev/pull/722) by [@khulnasoft](https://github.com/khulnasoft) including initial work in PR [#699](https://github.com/khulnasoft/sqldev/pull/699) by [@AntonDeMeester](https://github.com/AntonDeMeester).

## 0.0.13

### Fixes

* ♻️ Refactor type generation of selects re-order to prioritize models to optimize editor support. PR [#718](https://github.com/khulnasoft/sqldev/pull/718) by [@khulnasoft](https://github.com/khulnasoft).

### Refactors

* 🔇 Do not raise deprecation warnings for execute as it's automatically used internally. PR [#716](https://github.com/khulnasoft/sqldev/pull/716) by [@khulnasoft](https://github.com/khulnasoft).
* ✅ Move OpenAPI tests inline to simplify updating them with Pydantic v2. PR [#709](https://github.com/khulnasoft/sqldev/pull/709) by [@khulnasoft](https://github.com/khulnasoft).

### Upgrades

* ⬆️ Add support for Python 3.11 and Python 3.12. PR [#710](https://github.com/khulnasoft/sqldev/pull/710) by [@khulnasoft](https://github.com/khulnasoft).

### Docs

* ✏️ Fix typo, simplify single quote/apostrophe character in "Sister Margaret's" everywhere in the docs. PR [#721](https://github.com/khulnasoft/sqldev/pull/721) by [@khulnasoft](https://github.com/khulnasoft).
* 📝 Update docs for Decimal, use proper types. PR [#719](https://github.com/khulnasoft/sqldev/pull/719) by [@khulnasoft](https://github.com/khulnasoft).
* 📝 Add source examples for Python 3.9 and 3.10. PR [#715](https://github.com/khulnasoft/sqldev/pull/715) by [@khulnasoft](https://github.com/khulnasoft).

### Internal

* 🙈 Update gitignore, include all coverage files. PR [#711](https://github.com/khulnasoft/sqldev/pull/711) by [@khulnasoft](https://github.com/khulnasoft).
* 🔧 Update config with new pymdown extensions. PR [#712](https://github.com/khulnasoft/sqldev/pull/712) by [@khulnasoft](https://github.com/khulnasoft).
* 🔧 Update docs build setup, add support for sponsors, add sponsor GOVCERT.LU. PR [#720](https://github.com/khulnasoft/sqldev/pull/720) by [@khulnasoft](https://github.com/khulnasoft).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#697](https://github.com/khulnasoft/sqldev/pull/697) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* 🔧 Show line numbers in docs during local development. PR [#714](https://github.com/khulnasoft/sqldev/pull/714) by [@khulnasoft](https://github.com/khulnasoft).
* 📝 Update details syntax with new pymdown extensions format. PR [#713](https://github.com/khulnasoft/sqldev/pull/713) by [@khulnasoft](https://github.com/khulnasoft).

## 0.0.12

### Features

* ✨ Upgrade SQLAlchemy to 2.0. PR [#700](https://github.com/khulnasoft/sqldev/pull/700) by [@khulnasoft](https://github.com/khulnasoft) including initial work in PR [#563](https://github.com/khulnasoft/sqldev/pull/563) by [@farahats9](https://github.com/farahats9).

### Internal

* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#686](https://github.com/khulnasoft/sqldev/pull/686) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* 👷 Upgrade latest-changes GitHub Action. PR [#693](https://github.com/khulnasoft/sqldev/pull/693) by [@khulnasoft](https://github.com/khulnasoft).

## 0.0.11

### Features

* ✨ Add support for passing a custom SQLAlchemy type to `Field()` with `sa_type`. PR [#505](https://github.com/khulnasoft/sqldev/pull/505) by [@maru0123-2004](https://github.com/maru0123-2004).
    * You might consider this a breaking change if you were using an incompatible combination of arguments, those arguments were not taking effect and now you will have a type error and runtime error telling you that.
* ✨ Do not allow invalid combinations of field parameters for columns and relationships, `sa_column` excludes `sa_column_args`, `primary_key`, `nullable`, etc. PR [#681](https://github.com/khulnasoft/sqldev/pull/681) by [@khulnasoft](https://github.com/khulnasoft).

### Docs

* 🎨 Update inline source examples, hide `#` in annotations (from MkDocs Material). PR [#677](https://github.com/khulnasoft/sqldev/pull/677) by [@Matthieu-LAURENT39](https://github.com/Matthieu-LAURENT39).

### Internal

* ⬆ Update coverage requirement from ^6.2 to >=6.2,<8.0. PR [#663](https://github.com/khulnasoft/sqldev/pull/663) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Update mkdocs-material requirement from 9.1.21 to 9.2.7. PR [#675](https://github.com/khulnasoft/sqldev/pull/675) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Upgrade mypy manually. PR [#684](https://github.com/khulnasoft/sqldev/pull/684) by [@khulnasoft](https://github.com/khulnasoft).
* ⬆ Update black requirement from ^22.10.0 to >=22.10,<24.0. PR [#664](https://github.com/khulnasoft/sqldev/pull/664) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Update CI to build MkDocs Insiders only when the secrets are available, for Dependabot. PR [#683](https://github.com/khulnasoft/sqldev/pull/683) by [@khulnasoft](https://github.com/khulnasoft).

## 0.0.10

### Features

* ✨ Add support for all `Field` parameters from Pydantic `1.9.0` and above, make Pydantic `1.9.0` the minimum required version. PR [#440](https://github.com/khulnasoft/sqldev/pull/440) by [@daniil-berg](https://github.com/daniil-berg).

### Internal

* 🔧 Adopt Ruff for formatting. PR [#679](https://github.com/khulnasoft/sqldev/pull/679) by [@khulnasoft](https://github.com/khulnasoft).

## 0.0.9

### Breaking Changes

* 🗑️ Deprecate Python 3.6 and upgrade Poetry and Poetry Version Plugin. PR [#627](https://github.com/khulnasoft/sqldev/pull/627) by [@khulnasoft](https://github.com/khulnasoft).

### Features

* ✨ Raise a more clear error when a type is not valid. PR [#425](https://github.com/khulnasoft/sqldev/pull/425) by [@ddanier](https://github.com/ddanier).

### Fixes

* 🐛 Fix `AsyncSession` type annotations for `exec()`. PR [#58](https://github.com/khulnasoft/sqldev/pull/58) by [@Bobronium](https://github.com/Bobronium).
* 🐛 Fix allowing using a `ForeignKey` directly, remove repeated column construction from `SQLDevMetaclass.__init__` and upgrade minimum SQLAlchemy to `>=1.4.36`. PR [#443](https://github.com/khulnasoft/sqldev/pull/443) by [@daniil-berg](https://github.com/daniil-berg).
* 🐛 Fix enum type checks ordering in `get_sqlalchemy_type`. PR [#669](https://github.com/khulnasoft/sqldev/pull/669) by [@khulnasoft](https://github.com/khulnasoft).
* 🐛 Fix SQLAlchemy version 1.4.36 breaks SQLDev relationships (#315). PR [#461](https://github.com/khulnasoft/sqldev/pull/461) by [@byrman](https://github.com/byrman).

### Upgrades

* ⬆️ Upgrade support for SQLAlchemy 1.4.49, update tests. PR [#519](https://github.com/khulnasoft/sqldev/pull/519) by [@sandrotosi](https://github.com/sandrotosi).
* ⬆ Raise SQLAlchemy version requirement to at least `1.4.29` (related to #434). PR [#439](https://github.com/khulnasoft/sqldev/pull/439) by [@daniil-berg](https://github.com/daniil-berg).

### Docs

* 📝 Clarify description of in-memory SQLite database in `docs/tutorial/create-db-and-table.md`. PR [#601](https://github.com/khulnasoft/sqldev/pull/601) by [@SimonCW](https://github.com/SimonCW).
* 📝 Tweak wording in `docs/tutorial/fastapi/multiple-models.md`. PR [#674](https://github.com/khulnasoft/sqldev/pull/674) by [@khulnasoft](https://github.com/khulnasoft).
* ✏️ Fix contributing instructions to run tests, update script name. PR [#634](https://github.com/khulnasoft/sqldev/pull/634) by [@PookieBuns](https://github.com/PookieBuns).
* 📝 Update link to docs for intro to databases. PR [#593](https://github.com/khulnasoft/sqldev/pull/593) by [@abenezerBelachew](https://github.com/abenezerBelachew).
* 📝 Update docs, use `offset` in example with `limit` and `where`. PR [#273](https://github.com/khulnasoft/sqldev/pull/273) by [@jbmchuck](https://github.com/jbmchuck).
* 📝 Fix docs for Pydantic's fields using `le` (`lte` is invalid, use `le` ). PR [#207](https://github.com/khulnasoft/sqldev/pull/207) by [@jrycw](https://github.com/jrycw).
* 📝 Update outdated link in `docs/db-to-code.md`. PR [#649](https://github.com/khulnasoft/sqldev/pull/649) by [@MatveyF](https://github.com/MatveyF).
* ✏️ Fix typos found with codespell. PR [#520](https://github.com/khulnasoft/sqldev/pull/520) by [@kianmeng](https://github.com/kianmeng).
* 📝 Fix typos (duplication) in main page. PR [#631](https://github.com/khulnasoft/sqldev/pull/631) by [@Mr-DRP](https://github.com/Mr-DRP).
* 📝 Update release notes, add second author to PR. PR [#429](https://github.com/khulnasoft/sqldev/pull/429) by [@br-follow](https://github.com/br-follow).
* 📝 Update instructions about how to make a foreign key required in `docs/tutorial/relationship-attributes/define-relationships-attributes.md`. PR [#474](https://github.com/khulnasoft/sqldev/pull/474) by [@jalvaradosegura](https://github.com/jalvaradosegura).
* 📝 Update help SQLDev docs. PR [#548](https://github.com/khulnasoft/sqldev/pull/548) by [@khulnasoft](https://github.com/khulnasoft).
* ✏️ Fix typo in internal function name `get_sqlachemy_type()`. PR [#496](https://github.com/khulnasoft/sqldev/pull/496) by [@cmarqu](https://github.com/cmarqu).
* ✏️ Fix typo in docs. PR [#446](https://github.com/khulnasoft/sqldev/pull/446) by [@davidbrochart](https://github.com/davidbrochart).
* ✏️ Fix typo in `docs/tutorial/create-db-and-table.md`. PR [#477](https://github.com/khulnasoft/sqldev/pull/477) by [@FluffyDietEngine](https://github.com/FluffyDietEngine).
* ✏️ Fix small typos in docs. PR [#481](https://github.com/khulnasoft/sqldev/pull/481) by [@micuffaro](https://github.com/micuffaro).

### Internal

* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#672](https://github.com/khulnasoft/sqldev/pull/672) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump dawidd6/action-download-artifact from 2.24.2 to 2.28.0. PR [#660](https://github.com/khulnasoft/sqldev/pull/660) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ✅ Refactor OpenAPI FastAPI tests to simplify updating them later, this moves things around without changes. PR [#671](https://github.com/khulnasoft/sqldev/pull/671) by [@khulnasoft](https://github.com/khulnasoft).
* ⬆ Bump actions/checkout from 3 to 4. PR [#670](https://github.com/khulnasoft/sqldev/pull/670) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🔧 Update mypy config, use `strict = true` instead of manual configs. PR [#428](https://github.com/khulnasoft/sqldev/pull/428) by [@michaeloliverx](https://github.com/michaeloliverx).
* ⬆️ Upgrade MkDocs Material. PR [#668](https://github.com/khulnasoft/sqldev/pull/668) by [@khulnasoft](https://github.com/khulnasoft).
* 🎨 Update docs format and references with pre-commit and Ruff. PR [#667](https://github.com/khulnasoft/sqldev/pull/667) by [@khulnasoft](https://github.com/khulnasoft).
* 🎨 Run pre-commit on all files and autoformat. PR [#666](https://github.com/khulnasoft/sqldev/pull/666) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Move to Ruff and add pre-commit. PR [#661](https://github.com/khulnasoft/sqldev/pull/661) by [@khulnasoft](https://github.com/khulnasoft).
* 🛠️ Add `CITATION.cff` file for academic citations. PR [#13](https://github.com/khulnasoft/sqldev/pull/13) by [@sugatoray](https://github.com/sugatoray).
* 👷 Update docs deployments to Cloudflare. PR [#630](https://github.com/khulnasoft/sqldev/pull/630) by [@khulnasoft](https://github.com/khulnasoft).
* 👷‍♂️ Upgrade CI for docs. PR [#628](https://github.com/khulnasoft/sqldev/pull/628) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Update CI debug mode with Tmate. PR [#629](https://github.com/khulnasoft/sqldev/pull/629) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Update latest changes token. PR [#616](https://github.com/khulnasoft/sqldev/pull/616) by [@khulnasoft](https://github.com/khulnasoft).
* ⬆️ Upgrade analytics. PR [#558](https://github.com/khulnasoft/sqldev/pull/558) by [@khulnasoft](https://github.com/khulnasoft).
* 🔧 Update new issue chooser to point to GitHub Discussions. PR [#546](https://github.com/khulnasoft/sqldev/pull/546) by [@khulnasoft](https://github.com/khulnasoft).
* 🔧 Add template for GitHub Discussion questions and update issues template. PR [#544](https://github.com/khulnasoft/sqldev/pull/544) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Refactor CI artifact upload/download for docs previews. PR [#514](https://github.com/khulnasoft/sqldev/pull/514) by [@khulnasoft](https://github.com/khulnasoft).
* ⬆ Bump actions/cache from 2 to 3. PR [#497](https://github.com/khulnasoft/sqldev/pull/497) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump dawidd6/action-download-artifact from 2.24.0 to 2.24.2. PR [#493](https://github.com/khulnasoft/sqldev/pull/493) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🔧 Update Smokeshow coverage threshold. PR [#487](https://github.com/khulnasoft/sqldev/pull/487) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Move from Codecov to Smokeshow. PR [#486](https://github.com/khulnasoft/sqldev/pull/486) by [@khulnasoft](https://github.com/khulnasoft).
* ⬆ Bump actions/setup-python from 2 to 4. PR [#411](https://github.com/khulnasoft/sqldev/pull/411) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Update black requirement from ^21.5-beta.1 to ^22.10.0. PR [#460](https://github.com/khulnasoft/sqldev/pull/460) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ➕ Add extra dev dependencies for MkDocs Material. PR [#485](https://github.com/khulnasoft/sqldev/pull/485) by [@khulnasoft](https://github.com/khulnasoft).
* ⬆ Update mypy requirement from 0.930 to 0.971. PR [#380](https://github.com/khulnasoft/sqldev/pull/380) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Update coverage requirement from ^5.5 to ^6.2. PR [#171](https://github.com/khulnasoft/sqldev/pull/171) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump codecov/codecov-action from 2 to 3. PR [#415](https://github.com/khulnasoft/sqldev/pull/415) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/upload-artifact from 2 to 3. PR [#412](https://github.com/khulnasoft/sqldev/pull/412) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Update flake8 requirement from ^3.9.2 to ^5.0.4. PR [#396](https://github.com/khulnasoft/sqldev/pull/396) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Update pytest requirement from ^6.2.4 to ^7.0.1. PR [#242](https://github.com/khulnasoft/sqldev/pull/242) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/checkout from 2 to 3.1.0. PR [#458](https://github.com/khulnasoft/sqldev/pull/458) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump dawidd6/action-download-artifact from 2.9.0 to 2.24.0. PR [#470](https://github.com/khulnasoft/sqldev/pull/470) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Update Dependabot config. PR [#484](https://github.com/khulnasoft/sqldev/pull/484) by [@khulnasoft](https://github.com/khulnasoft).

## 0.0.8

### Fixes

* 🐛 Fix auto detecting and setting `nullable`, allowing overrides in field. PR [#423](https://github.com/khulnasoft/sqldev/pull/423) by [@JonasKs](https://github.com/JonasKs) and [@br-follow](https://github.com/br-follow).
* ♻️ Update `expresion.py`, sync from Jinja2 template, implement `inherit_cache` to solve errors like: `SAWarning: Class SelectOfScalar will not make use of SQL compilation caching`. PR [#422](https://github.com/khulnasoft/sqldev/pull/422) by [@khulnasoft](https://github.com/khulnasoft).

### Docs

* 📝 Adjust and clarify docs for `docs/tutorial/create-db-and-table.md`. PR [#426](https://github.com/khulnasoft/sqldev/pull/426) by [@khulnasoft](https://github.com/khulnasoft).
* ✏ Fix typo in `docs/tutorial/connect/remove-data-connections.md`. PR [#421](https://github.com/khulnasoft/sqldev/pull/421) by [@VerdantFox](https://github.com/VerdantFox).

## 0.0.7

### Features

* ✨ Allow setting `unique` in `Field()` for a column. PR [#83](https://github.com/khulnasoft/sqldev/pull/83) by [@raphaelgibson](https://github.com/raphaelgibson).
* ✨ Update GUID handling to use stdlib `UUID.hex` instead of an `int`. PR [#26](https://github.com/khulnasoft/sqldev/pull/26) by [@andrewbolster](https://github.com/andrewbolster).
* ✨ Raise an exception when using a Pydantic field type with no matching SQLAlchemy type. PR [#18](https://github.com/khulnasoft/sqldev/pull/18) by [@elben10](https://github.com/elben10).
* ⬆ Upgrade constrain for SQLAlchemy = ">=1.4.17,<=1.4.41". PR [#371](https://github.com/khulnasoft/sqldev/pull/371) by [@RobertRosca](https://github.com/RobertRosca).
* ✨ Add new `Session.get()` parameter `execution_options`. PR [#302](https://github.com/khulnasoft/sqldev/pull/302) by [@khulnasoft](https://github.com/khulnasoft).

### Fixes

* 🐛 Fix type annotations for `Model.parse_obj()`, and `Model.validate()`. PR [#321](https://github.com/khulnasoft/sqldev/pull/321) by [@phi-friday](https://github.com/phi-friday).
* 🐛 Fix `Select` and `SelectOfScalar` to inherit cache to avoid warning: `SAWarning: Class SelectOfScalar will not make use of SQL compilation caching`. PR [#234](https://github.com/khulnasoft/sqldev/pull/234) by [@rabinadk1](https://github.com/rabinadk1).
* 🐛 Fix handling validators for non-default values. PR [#253](https://github.com/khulnasoft/sqldev/pull/253) by [@byrman](https://github.com/byrman).
* 🐛 Fix fields marked as "set" in models. PR [#117](https://github.com/khulnasoft/sqldev/pull/117) by [@statt8900](https://github.com/statt8900).
* 🐛 Fix Enum handling in SQLAlchemy. PR [#165](https://github.com/khulnasoft/sqldev/pull/165) by [@chriswhite199](https://github.com/chriswhite199).
* 🐛 Fix setting nullable property of Fields that don't accept `None`. PR [#79](https://github.com/khulnasoft/sqldev/pull/79) by [@van51](https://github.com/van51).
* 🐛 Fix SQLAlchemy version 1.4.36 breaks SQLDev relationships (#315). PR [#322](https://github.com/khulnasoft/sqldev/pull/322) by [@byrman](https://github.com/byrman).

### Docs

* 📝 Update docs for models for updating, `id` should not be updatable. PR [#335](https://github.com/khulnasoft/sqldev/pull/335) by [@kurtportelli](https://github.com/kurtportelli).
* ✏ Fix broken variable/typo in docs for Read Relationships, `hero_spider_boy.id` => `hero_spider_boy.team_id`. PR [#106](https://github.com/khulnasoft/sqldev/pull/106) by [@yoannmos](https://github.com/yoannmos).
* 🎨 Remove unwanted highlight in the docs. PR [#233](https://github.com/khulnasoft/sqldev/pull/233) by [@jalvaradosegura](https://github.com/jalvaradosegura).
* ✏ Fix typos in `docs/databases.md` and `docs/tutorial/index.md`. PR [#35](https://github.com/khulnasoft/sqldev/pull/35) by [@prrao87](https://github.com/prrao87).
* ✏ Fix typo in `docs/tutorial/relationship-attributes/define-relationships-attributes.md`. PR [#239](https://github.com/khulnasoft/sqldev/pull/239) by [@jalvaradosegura](https://github.com/jalvaradosegura).
* ✏ Fix typo in `docs/tutorial/fastapi/simple-hero-api.md`. PR [#80](https://github.com/khulnasoft/sqldev/pull/80) by [@joemudryk](https://github.com/joemudryk).
* ✏ Fix typos in multiple files in the docs. PR [#400](https://github.com/khulnasoft/sqldev/pull/400) by [@VictorGambarini](https://github.com/VictorGambarini).
* ✏ Fix typo in `docs/tutorial/code-structure.md`. PR [#344](https://github.com/khulnasoft/sqldev/pull/344) by [@marciomazza](https://github.com/marciomazza).
* ✏ Fix typo in `docs/db-to-code.md`. PR [#155](https://github.com/khulnasoft/sqldev/pull/155) by [@gr8jam](https://github.com/gr8jam).
* ✏ Fix typo in `docs/contributing.md`. PR [#323](https://github.com/khulnasoft/sqldev/pull/323) by [@Fardad13](https://github.com/Fardad13).
* ✏ Fix typo in `docs/tutorial/fastapi/tests.md`. PR [#265](https://github.com/khulnasoft/sqldev/pull/265) by [@johnhoman](https://github.com/johnhoman).
* ✏ Fix typo in `docs/tutorial/where.md`. PR [#286](https://github.com/khulnasoft/sqldev/pull/286) by [@jalvaradosegura](https://github.com/jalvaradosegura).
* ✏ Fix typos in `docs/tutorial/fastapi/update.md`. PR [#268](https://github.com/khulnasoft/sqldev/pull/268) by [@cirrusj](https://github.com/cirrusj).
* ✏ Fix typo in `docs/tutorial/fastapi/simple-hero-api.md`. PR [#247](https://github.com/khulnasoft/sqldev/pull/247) by [@hao-wang](https://github.com/hao-wang).
* ✏ Fix typos in `docs/tutorial/automatic-id-none-refresh.md`, `docs/tutorial/fastapi/update.md`, `docs/tutorial/select.md`. PR [#185](https://github.com/khulnasoft/sqldev/pull/185) by [@rootux](https://github.com/rootux).
* ✏ Fix typo in `docs/databases.md`. PR [#177](https://github.com/khulnasoft/sqldev/pull/177) by [@seandlg](https://github.com/seandlg).
* ✏ Fix typos in `docs/tutorial/fastapi/update.md`. PR [#162](https://github.com/khulnasoft/sqldev/pull/162) by [@wmcgee3](https://github.com/wmcgee3).
* ✏ Fix typos in `docs/tutorial/code-structure.md`, `docs/tutorial/fastapi/multiple-models.md`, `docs/tutorial/fastapi/simple-hero-api.md`, `docs/tutorial/many-to-many/index.md`. PR [#116](https://github.com/khulnasoft/sqldev/pull/116) by [@moonso](https://github.com/moonso).
* ✏ Fix typo in `docs/tutorial/fastapi/teams.md`. PR [#154](https://github.com/khulnasoft/sqldev/pull/154) by [@chrisgoddard](https://github.com/chrisgoddard).
* ✏ Fix typo variable in example about relationships and `back_populates`, always use `hero` instead of `owner`. PR [#120](https://github.com/khulnasoft/sqldev/pull/120) by [@onionj](https://github.com/onionj).
* ✏ Fix typo in `docs/tutorial/fastapi/tests.md`. PR [#113](https://github.com/khulnasoft/sqldev/pull/113) by [@feanil](https://github.com/feanil).
* ✏ Fix typo in `docs/tutorial/where.md`. PR [#72](https://github.com/khulnasoft/sqldev/pull/72) by [@ZettZet](https://github.com/ZettZet).
* ✏ Fix typo in `docs/tutorial/code-structure.md`. PR [#91](https://github.com/khulnasoft/sqldev/pull/91) by [@dhiraj](https://github.com/dhiraj).
* ✏ Fix broken link to newsletter sign-up in `docs/help.md`. PR [#84](https://github.com/khulnasoft/sqldev/pull/84) by [@mborus](https://github.com/mborus).
* ✏ Fix typos in `docs/tutorial/many-to-many/create-models-with-link.md`. PR [#45](https://github.com/khulnasoft/sqldev/pull/45) by [@xginn8](https://github.com/xginn8).
* ✏ Fix typo in `docs/tutorial/index.md`. PR [#398](https://github.com/khulnasoft/sqldev/pull/398) by [@ryangrose](https://github.com/ryangrose).

### Internal

* ♻ Refactor internal statements to simplify code. PR [#53](https://github.com/khulnasoft/sqldev/pull/53) by [@yezz123](https://github.com/yezz123).
* ♻ Refactor internal imports to reduce redundancy. PR [#272](https://github.com/khulnasoft/sqldev/pull/272) by [@aminalaee](https://github.com/aminalaee).
* ⬆ Update development requirement for FastAPI from `^0.68.0` to `^0.68.1`. PR [#48](https://github.com/khulnasoft/sqldev/pull/48) by [@alucarddelta](https://github.com/alucarddelta).
* ⏪ Revert upgrade Poetry, to make a release that supports Python 3.6 first. PR [#417](https://github.com/khulnasoft/sqldev/pull/417) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Add dependabot for GitHub Actions. PR [#410](https://github.com/khulnasoft/sqldev/pull/410) by [@khulnasoft](https://github.com/khulnasoft).
* ⬆️ Upgrade Poetry to version `==1.2.0b1`. PR [#303](https://github.com/khulnasoft/sqldev/pull/303) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Add CI for Python 3.10. PR [#305](https://github.com/khulnasoft/sqldev/pull/305) by [@khulnasoft](https://github.com/khulnasoft).
* 📝 Add Jina's QA Bot to the docs to help people that want to ask quick questions. PR [#263](https://github.com/khulnasoft/sqldev/pull/263) by [@khulnasoft](https://github.com/khulnasoft).
* 👷 Upgrade Codecov GitHub Action. PR [#304](https://github.com/khulnasoft/sqldev/pull/304) by [@khulnasoft](https://github.com/khulnasoft).
* 💚 Only run CI on push when on master, to avoid duplicate runs on PRs. PR [#244](https://github.com/khulnasoft/sqldev/pull/244) by [@khulnasoft](https://github.com/khulnasoft).
* 🔧 Upgrade MkDocs Material and update configs. PR [#217](https://github.com/khulnasoft/sqldev/pull/217) by [@khulnasoft](https://github.com/khulnasoft).
* ⬆ Upgrade mypy, fix type annotations. PR [#218](https://github.com/khulnasoft/sqldev/pull/218) by [@khulnasoft](https://github.com/khulnasoft).

## 0.0.6

### Breaking Changes

**SQLDev** no longer creates indexes by default for every column, indexes are now opt-in. You can read more about it in PR [#205](https://github.com/khulnasoft/sqldev/pull/205).

Before this change, if you had a model like this:

```Python
from typing import Optional

from sqldev import Field, SQLDev


class Hero(SQLDev, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None
```

...when creating the tables, SQLDev version `0.0.5` and below, would also create an index for `name`, one for `secret_name`, and one for `age` (`id` is the primary key, so it doesn't need an additional index).

If you depended on having an index for each one of those columns, now you can (and would have to) define them explicitly:

```Python
class Hero(SQLDev, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str = Field(index=True)
    age: Optional[int] = Field(default=None, index=True)
```

There's a high chance you don't need indexes for all the columns. For example, you might only need indexes for `name` and `age`, but not for `secret_name`. In that case, you could define the model as:

```Python
class Hero(SQLDev, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)
```

If you already created your database tables with SQLDev using versions `0.0.5` or below, it would have also created those indexes in the database. In that case, you might want to manually drop (remove) some of those indexes, if they are unnecessary, to avoid the extra cost in performance and space.

Depending on the database you are using, there will be a different way to find the available indexes.

For example, let's say you no longer need the index for `secret_name`. You could check the current indexes in the database and find the one for `secret_name`, it could be named `ix_hero_secret_name`. Then you can remove it with SQL:

```SQL
DROP INDEX ix_hero_secret_name
```

or

```SQL
DROP INDEX ix_hero_secret_name ON hero;
```

Here's the new, extensive documentation explaining indexes and how to use them: [Indexes - Optimize Queries](https://sqldev.khulnasoft.com/tutorial/indexes/).

### Docs

* ✨ Document indexes and make them opt-in. Here's the new documentation: [Indexes - Optimize Queries](https://sqldev.khulnasoft.com/tutorial/indexes/). This is the same change described above in **Breaking Changes**. PR [#205](https://github.com/khulnasoft/sqldev/pull/205) by [@khulnasoft](https://github.com/khulnasoft).
* ✏ Fix typo in FastAPI tutorial. PR [#192](https://github.com/khulnasoft/sqldev/pull/192) by [@yaquelinehoyos](https://github.com/yaquelinehoyos).
* 📝 Add links to the license file. PR [#29](https://github.com/khulnasoft/sqldev/pull/29) by [@sobolevn](https://github.com/sobolevn).
* ✏ Fix typos in docs titles. PR [#28](https://github.com/khulnasoft/sqldev/pull/28) by [@Batalex](https://github.com/Batalex).
* ✏ Fix multiple typos and some rewording. PR [#22](https://github.com/khulnasoft/sqldev/pull/22) by [@egrim](https://github.com/egrim).
* ✏ Fix typo in `docs/tutorial/automatic-id-none-refresh.md`. PR [#14](https://github.com/khulnasoft/sqldev/pull/14) by [@leynier](https://github.com/leynier).
* ✏ Fix typos in `docs/tutorial/index.md` and `docs/databases.md`. PR [#5](https://github.com/khulnasoft/sqldev/pull/5) by [@sebastianmarines](https://github.com/sebastianmarines).

## 0.0.5

### Features

* ✨ Add support for Decimal fields from Pydantic and SQLAlchemy. Original PR [#103](https://github.com/khulnasoft/sqldev/pull/103) by [@robcxyz](https://github.com/robcxyz). New docs: [Advanced User Guide - Decimal Numbers](https://sqldev.khulnasoft.com/advanced/decimal/).

### Docs

* ✏ Update decimal tutorial source for consistency. PR [#188](https://github.com/khulnasoft/sqldev/pull/188) by [@khulnasoft](https://github.com/khulnasoft).

### Internal

* 🔧 Split MkDocs insiders build in CI to support building from PRs. PR [#186](https://github.com/khulnasoft/sqldev/pull/186) by [@khulnasoft](https://github.com/khulnasoft).
* 🎨 Format `expression.py` and expression template, currently needed by CI. PR [#187](https://github.com/khulnasoft/sqldev/pull/187) by [@khulnasoft](https://github.com/khulnasoft).
* 🐛Fix docs light/dark theme switcher. PR [#1](https://github.com/khulnasoft/sqldev/pull/1) by [@Lehoczky](https://github.com/Lehoczky).
* 🔧 Add MkDocs Material social cards. PR [#90](https://github.com/khulnasoft/sqldev/pull/90) by [@khulnasoft](https://github.com/khulnasoft).
* ✨ Update type annotations and upgrade mypy. PR [#173](https://github.com/khulnasoft/sqldev/pull/173) by [@khulnasoft](https://github.com/khulnasoft).

## 0.0.4

* 🎨 Fix type detection of select results in PyCharm. PR [#15](https://github.com/khulnasoft/sqldev/pull/15) by [@khulnasoft](https://github.com/khulnasoft).

## 0.0.3

* ⬆️ Update and relax specification range for `sqlalchemy-stubs`. PR [#4](https://github.com/khulnasoft/sqldev/pull/4) by [@khulnasoft](https://github.com/khulnasoft).

## 0.0.2

* This includes several small bug fixes detected during the first CI runs.
* 💚 Fix CI installs and tests. PR [#2](https://github.com/khulnasoft/sqldev/pull/2) by [@khulnasoft](https://github.com/khulnasoft).

## 0.0.1

* First release. 🎉
