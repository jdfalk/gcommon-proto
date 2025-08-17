# [1.0.0](https://github.com/jdfalk/gcommon/compare/v0.1.1...v1.0.0) (2025-08-15)

### Bug Fixes

- Add teh google protos that are missing. fix the common path ([5da15ab](https://github.com/jdfalk/gcommon/commit/5da15ab019b78b435cd1c5f2d7b6ea9284b32752))
- **auth:** add missing role.proto imports across multiple proto files ([61540bb](https://github.com/jdfalk/gcommon/commit/61540bb4a3743d4b391c380334fbd191948f93d9))
- **auth:** add script to fix missing imports in auth service files ([7a69bcc](https://github.com/jdfalk/gcommon/commit/7a69bcc2f46477c9b224a09d8880474d53a68d2d))
- **auth:** consolidate MFA enum duplicates and add missing service imports ([298320a](https://github.com/jdfalk/gcommon/commit/298320a2aabb199dffcdebd73e19273e47cc4f0f))
- **auth:** resolve import issues and malformed imports ([08bcd8e](https://github.com/jdfalk/gcommon/commit/08bcd8e7072eca436feefdb851194801f7b71ce4))
- **ci:** grant projects permission for unified automation ([792ca9b](https://github.com/jdfalk/gcommon/commit/792ca9bb96c54ac24036889dbcc000827924058b))
- **ci:** handle deferred type hints in config serialization ([33b1827](https://github.com/jdfalk/gcommon/commit/33b1827c54c4c284f5c8cc6812a69e1c8f248e52))
- **ci:** sync improved super-linter log file handling from ghcommon ([c00f823](https://github.com/jdfalk/gcommon/commit/c00f82363ee800d43932c9103711d63e1c4c8dc9))
- clean up formatting and improve clarity in SESSION_STATUS_HANDOFF.md ([66324ac](https://github.com/jdfalk/gcommon/commit/66324ac9c6e6d61de14410cd28e241e7df2f49c8))
- Clean up whitespace and reorder imports in configuration and script files ([95f144d](https://github.com/jdfalk/gcommon/commit/95f144d8091fb5944e738e4503fd582637d7f06c))
- **config:** update protobuf generated files ([38a3e75](https://github.com/jdfalk/gcommon/commit/38a3e75fadfd64741218d26aea11c16de1f0da02))
- configure markdownlint symlink for consistent config usage ([d7ed429](https://github.com/jdfalk/gcommon/commit/d7ed429b8dd9c52e448ebe7809e4a4a3d537b77c))
- correct type reference for batch processing options in batch_operation.proto ([8cddda3](https://github.com/jdfalk/gcommon/commit/8cddda30d0a0c0e886c250766c7c59b296143baa))
- format code for consistency and readability in health check script ([7d3f2b7](https://github.com/jdfalk/gcommon/commit/7d3f2b723820e950047360e5e287a0eae78b03c3))
- formatting stuff in the protos. ([4d1e383](https://github.com/jdfalk/gcommon/commit/4d1e383824ef70872683504d29718e74d5fd3c82))
- formatting stuff in the protos. ([e11a6e0](https://github.com/jdfalk/gcommon/commit/e11a6e021abebc64c64491cd05fae73c85ce7a23))
- formatting stuff in the protos. ([c1560f2](https://github.com/jdfalk/gcommon/commit/c1560f27a421de0044bff8c5eb088dde48de754b))
- formatting stuff in the protos. ([6ea87d0](https://github.com/jdfalk/gcommon/commit/6ea87d03747bfef635f3485368ecbcd6fb533173))
- **gitignore:** fix .vscode ignore order to allow tasks.json ([243aed4](https://github.com/jdfalk/gcommon/commit/243aed47a5a55f1b10c02ea988bacfa62b703ada))
- **go.mod:** update gopkg.in/yaml.v3 requirement to remove indirect comment ([1a68905](https://github.com/jdfalk/gcommon/commit/1a68905ee29bc2c00c0180639843347e663d0ab2))
- **health:** remove duplicate imports and fix malformed import paths ([6b049b7](https://github.com/jdfalk/gcommon/commit/6b049b753a2cbd35759c642407d481e220d9958d))
- Implement code changes to enhance functionality and improve performance ([9258fbc](https://github.com/jdfalk/gcommon/commit/9258fbc1d2f6a6e46218aba0f11b4d1997680099))
- Implement code changes to enhance functionality and improve performance ([4b53409](https://github.com/jdfalk/gcommon/commit/4b53409628ea8ff1e290bfca9737563ac285a2fa))
- import all request types in metrics admin service, update syntax to proto3 ([915936f](https://github.com/jdfalk/gcommon/commit/915936f6b3283f4fa29f46dc31feaaccda9b0dda))
- **metrics:** resolve import dependencies and implement MetricFilter ([62436b1](https://github.com/jdfalk/gcommon/commit/62436b1a793fece6237c5a04059377badc9466b7))
- **protbufs:** convert them all to the correct paths because it's stupid. ([6c94334](https://github.com/jdfalk/gcommon/commit/6c943349cff6f0a2d5d63485021dfa5741ac9f94))
- **protobuf:** commit any remaining protobuf-related changes ([13f8ad3](https://github.com/jdfalk/gcommon/commit/13f8ad3d22c16e6761cde5a32aeba7cfd01aa67c))
- **protobufs:** Change paths option to source_relative for better compatibility ([3d78c99](https://github.com/jdfalk/gcommon/commit/3d78c99a7f44e59006518c0eaa90892486865bcb))
- **protobufs:** Update generation location to be go compliant. ([6a30640](https://github.com/jdfalk/gcommon/commit/6a3064035653cd23dfb78615e2666d6ba86e64cb))
- **protobufs:** updated paths. ([139651b](https://github.com/jdfalk/gcommon/commit/139651bd1813a30bbb7b34c20cefb1a73fc5076a))
- **protobuf:** update auth module proto definitions ([3f10536](https://github.com/jdfalk/gcommon/commit/3f10536354a8843d5a103d59b241d14d9fae8396))
- **protobuf:** update common module proto definitions ([4895844](https://github.com/jdfalk/gcommon/commit/489584429060a7d565558f5b675116d5057d7f7b))
- **protobuf:** update config module proto definitions ([7b65b90](https://github.com/jdfalk/gcommon/commit/7b65b90dd2fb0768c4e7d318a6f697449ba5799e))
- **protobuf:** update health, cache, and db module proto definitions ([25e6e47](https://github.com/jdfalk/gcommon/commit/25e6e4705b9d82d56dcca55dfee9ab82f2951594))
- **protobuf:** update metrics module proto definitions ([3b5aceb](https://github.com/jdfalk/gcommon/commit/3b5aceba75ce7a47f74e68c0b8646b2078413e1b))
- **protobuf:** update organization and web module proto definitions ([6afa155](https://github.com/jdfalk/gcommon/commit/6afa155fd59817c1182cf25bdaa5478c8fb7d7e5))
- **protobuf:** update queue module proto definitions ([80b06b9](https://github.com/jdfalk/gcommon/commit/80b06b9663d69f0c08e9e9cac88a07f58e2c86fe))
- **protobuf:** update remaining module proto definitions ([8cab7a5](https://github.com/jdfalk/gcommon/commit/8cab7a55ac9bb371c938cfc59b1ab871f48dd51d))
- **proto:** Cache module import fixes ([98479a1](https://github.com/jdfalk/gcommon/commit/98479a128b005bb7f446a4c524da7187750cd899))
- **proto:** Config module import and type fixes - ConfigHealthCheckRequest/Response ([bdf8352](https://github.com/jdfalk/gcommon/commit/bdf835245b994df6df2057258bc4474addae236d))
- **proto:** correct import paths for error and health_status proto files ([61222c0](https://github.com/jdfalk/gcommon/commit/61222c0efa92d29a54726d2c1c30cdb498272476))
- **proto:** Database module import and type fixes - qualified types and isolation levels ([a1f1cfa](https://github.com/jdfalk/gcommon/commit/a1f1cfab5852a713c64e1ae0493675e5e632e9f4))
- **proto:** Health module import and type fixes - MetricsHealthCheckRequest ([8bd6983](https://github.com/jdfalk/gcommon/commit/8bd6983db0e84b4a27f8f975da73eaaf2aec3c9c))
- **proto:** Metrics module import and type fixes - MetricsAPIKeyConfig ([96e30b8](https://github.com/jdfalk/gcommon/commit/96e30b82ff673cc1293252e5a3d6c8a3358a6258))
- **proto:** Organization module import and type fixes - OrganizationResourceLimits ([dcb6535](https://github.com/jdfalk/gcommon/commit/dcb6535a076e10193fdc013ce641715cd4b8e6e7))
- **proto:** Queue module import and type fixes - ConfigConflictResolution ([a670c39](https://github.com/jdfalk/gcommon/commit/a670c39f32e3438a79cdc7d254d9b7e2c9b59d25))
- **proto:** remove incorrect import statement in response_metadata.proto ([da7681f](https://github.com/jdfalk/gcommon/commit/da7681ff18c21acfb168561fadc4749d9fa027f3))
- **proto:** remove unnecessary import from config_schema.proto ([16da79d](https://github.com/jdfalk/gcommon/commit/16da79db5f75c3b6daf66e41751a4d26bde8fd65))
- **proto:** resolve critical service and import path issues ([f419abf](https://github.com/jdfalk/gcommon/commit/f419abf45a77bd211a035c218442a743c7a6a8c2))
- **proto:** resolve import and type qualification issues in metrics, organization, and queue modules ([b01bae0](https://github.com/jdfalk/gcommon/commit/b01bae0641c70abea6990fdf4ad2030bf4481a56))
- **proto:** resolve major compilation issues without affecting missing type implementations ([19fe975](https://github.com/jdfalk/gcommon/commit/19fe975410c1db4507a44f68162c40729fb71bf8))
- **proto:** resolve remaining import and type qualification issues ([67c9a17](https://github.com/jdfalk/gcommon/commit/67c9a17128ed5246d5794d92363eab8d1f839a46))
- **proto:** restore import for session_status in session.proto ([39ac7f0](https://github.com/jdfalk/gcommon/commit/39ac7f0e8fa3dd5d513caff9bd0da69b6f7d597b))
- **proto:** Web module import and type fixes - WebCacheConfig and WebTLSConfig ([bac0111](https://github.com/jdfalk/gcommon/commit/bac0111ff3bd718f3acf1ca622042f6168369319))
- **queue:** correct monitoring metrics references ([8bab42f](https://github.com/jdfalk/gcommon/commit/8bab42f88217acd95e8986fb746f77437b6c91f1))
- **queue:** remove duplicate message definitions and fix imports ([790d20f](https://github.com/jdfalk/gcommon/commit/790d20f4069fd5f5ae72a9b2edaf54ea12fc1a12))
- **queue:** standardize go_package paths and fix import issues ([0cedbe1](https://github.com/jdfalk/gcommon/commit/0cedbe1130b8c0e19c407a0c75b63eb6612b080b))
- Readd removed google proto import. ([4e2e15a](https://github.com/jdfalk/gcommon/commit/4e2e15ac2f3a370de4c8257a4d5c4810e53c3d38))
- remove deprecated go_features.proto and go_features.pb.go files ([02ffde7](https://github.com/jdfalk/gcommon/commit/02ffde7c8bf668c03988b05ab4b5914d316edb15))
- remove duplicate metric_series.proto, fix imports in metrics service and query_metrics_request, create record_metrics_request ([f44040f](https://github.com/jdfalk/gcommon/commit/f44040fda4906f39621c1d94bcdbe025b5c73e30))
- remove duplicate super-linter workflow ([3fa8ff3](https://github.com/jdfalk/gcommon/commit/3fa8ff3643944cf723f182996a4f3fa5dd02ef62))
- remove unnecessary blank lines in alertmanager and prometheus YAML files ([c4f65e1](https://github.com/jdfalk/gcommon/commit/c4f65e11abf124177b85395d39370779b29b585f))
- remove unnecessary whitespace in PR automation script ([409e27e](https://github.com/jdfalk/gcommon/commit/409e27e79f5621250747a1706028147377bed6f3))
- reorder import statements in proto files for consistency ([3e0d5b8](https://github.com/jdfalk/gcommon/commit/3e0d5b8acc478ac86b4081a85daf20e2862382b4))
- repair issue system - 11 fixes applied ([496ceee](https://github.com/jdfalk/gcommon/commit/496ceee7af132c1e05e87123fa65fc143e842dd1))
- resolve actionlint shellcheck errors in consolidated workflow ([58a583e](https://github.com/jdfalk/gcommon/commit/58a583ebc7ad3d09f38f0175e687de7d8466526c))
- resolve circular import cycles and add remaining organization imports ([e721aa2](https://github.com/jdfalk/gcommon/commit/e721aa2191d94d54ea8f15794c0736c634bb5edc))
- resolve config_service.proto import errors ([6cf7514](https://github.com/jdfalk/gcommon/commit/6cf7514fd34fa0334650c61842cb6b12d7ad297e))
- resolve malformed import paths in version-related proto files ([0de1cc3](https://github.com/jdfalk/gcommon/commit/0de1cc37eacce1e98b9c281f3fd076dbf98a9345))
- resolve multiple protobuf import path errors ([c89ad04](https://github.com/jdfalk/gcommon/commit/c89ad04bb11a6973997ef76a999803d2d861af57))
- resolve protobuf compilation issues - batch 2 ([2b1b8f5](https://github.com/jdfalk/gcommon/commit/2b1b8f55901aa4d388164fe4fe24123adb432efc))
- resolve protobuf import errors and missing type references ([ec89a6f](https://github.com/jdfalk/gcommon/commit/ec89a6f1ba58dac45a0569d3d8ade87d73a01e4b))
- resolve protobuf import issues and missing message types ([9c578aa](https://github.com/jdfalk/gcommon/commit/9c578aae0a630d1c659aafd0d0b01f5081695b48))
- resolve security workflow issues ([7d28740](https://github.com/jdfalk/gcommon/commit/7d2874011808ce186f9b469e5cf4cbeec1d76918))
- **scripts:** allow issue updates without GH token ([09b7e0f](https://github.com/jdfalk/gcommon/commit/09b7e0fabf72da2e77f965cc74aa0dc929016611))
- **script:** update version to 2.0.1 and clarify GitHub issue check handling ([0169b73](https://github.com/jdfalk/gcommon/commit/0169b73a47c2a78cacf785b7a0cfddecc34aee88))
- specify github-token in secrets for PR automation jobs ([dd7562d](https://github.com/jdfalk/gcommon/commit/dd7562dd34921de93432e3ed5f7b2d1fa03589c4))
- standardize file headers and resolve duplicate imports ([a0daf06](https://github.com/jdfalk/gcommon/commit/a0daf063aaf6d734fae69d51e0b35dcbe44f2c19))
- standardize JSON formatting in issue updates ([8511b3b](https://github.com/jdfalk/gcommon/commit/8511b3b3193b2dd8dfd6d8149ea47a1fd23930d7))
- standardize quotes in workflow YAML files for consistency ([56b9896](https://github.com/jdfalk/gcommon/commit/56b98967410d8c6682c8f1f6b22a4967ff2ee095))
- standardize string delimiters in regex patterns for consistency ([771bd01](https://github.com/jdfalk/gcommon/commit/771bd01ed73b561ec0a146599f86fd280989ec6d))
- super-linter configuration issues ([51ef4e9](https://github.com/jdfalk/gcommon/commit/51ef4e9ce4bbd075b36efd3f763312d6116fd844))
- systematic protobuf import fixes ([38b551c](https://github.com/jdfalk/gcommon/commit/38b551c5993e3eeb5d6a96397e4944122a28bcd2))
- systematic protobuf import fixes ([e70c1be](https://github.com/jdfalk/gcommon/commit/e70c1be524928c9dc10043f194edf47553440eb1))
- systematic protobuf import fixes ([c11e898](https://github.com/jdfalk/gcommon/commit/c11e898095511149d751e1b56127b212f3943497))
- systematic protobuf import fixes ([477e197](https://github.com/jdfalk/gcommon/commit/477e197ed8a85e125dadbdd8addbdc40a5888e86))
- systematic protobuf import fixes ([c4664e5](https://github.com/jdfalk/gcommon/commit/c4664e58bcdc773d7c222e2243809d86024a3000))
- systematic protobuf import fixes ([a4571c1](https://github.com/jdfalk/gcommon/commit/a4571c1164970b3bf0e8e3f5a1d5eef8f3c85163))
- systematic protobuf import fixes ([2190fb2](https://github.com/jdfalk/gcommon/commit/2190fb214ef148cbac95c2e890ca0541e923c985))
- systematic protobuf import fixes ([6b829cb](https://github.com/jdfalk/gcommon/commit/6b829cbd748f69f6298ac7d44ba9e40c0ca01d19))
- systematic protobuf import fixes ([563e8e8](https://github.com/jdfalk/gcommon/commit/563e8e8f2ecd8854820acce4e35b0a6367da4b3d))
- systematic protobuf import fixes ([cc95dac](https://github.com/jdfalk/gcommon/commit/cc95dac1542d339dd7889fbdbe54841fddf03b5f))
- systematic protobuf import fixes ([bc4f9e6](https://github.com/jdfalk/gcommon/commit/bc4f9e64ced9026e6a5e47382d1b561b014be246))
- systematic protobuf import fixes ([dccbccf](https://github.com/jdfalk/gcommon/commit/dccbccf4130a8c10da241fc1324595207816deea))
- systematic protobuf import fixes ([b2c81ae](https://github.com/jdfalk/gcommon/commit/b2c81ae47024acd82badf1d955a6bc31cd27856f))
- systematic protobuf import fixes ([25125f3](https://github.com/jdfalk/gcommon/commit/25125f3a35c203a8f6d36cf3d0f621498c39183b))
- systematic protobuf import fixes ([c7e60bd](https://github.com/jdfalk/gcommon/commit/c7e60bdcc9116be16e8ad5d021b83077dcd04d98))
- systematic protobuf import fixes ([dc0709c](https://github.com/jdfalk/gcommon/commit/dc0709c24730f437ff232552c09be108fba1d18c))
- systematic protobuf import fixes ([9f64409](https://github.com/jdfalk/gcommon/commit/9f644097321ae87ac8e1f538c1774192b1840386))
- systematic protobuf import fixes ([b32c0b7](https://github.com/jdfalk/gcommon/commit/b32c0b73427c20b3458760520a25e586e03501dd))
- systematic protobuf import fixes ([d316862](https://github.com/jdfalk/gcommon/commit/d31686296cb5099368969f840a34716c3e197a82))
- systematic protobuf import fixes ([67556a6](https://github.com/jdfalk/gcommon/commit/67556a6e07dadc8889360250a1ceb2ab10ef0a41))
- systematic protobuf import fixes ([ba8e398](https://github.com/jdfalk/gcommon/commit/ba8e3983fb407792704184e44085a2bc4331b6df))
- systematic protobuf import fixes ([5d0a9b3](https://github.com/jdfalk/gcommon/commit/5d0a9b32728f8e745952ee9e20e723c058fc0214))
- systematic protobuf import fixes ([83c2961](https://github.com/jdfalk/gcommon/commit/83c2961eea322fc3e4a90a3074f5f014a64c263f))
- systematic protobuf import fixes ([d519083](https://github.com/jdfalk/gcommon/commit/d5190836b67e420f5eb2aa75175502042d737098))
- systematic protobuf import fixes ([04412eb](https://github.com/jdfalk/gcommon/commit/04412eb20b3bba74bdb1d9be55e00a783d4a945d))
- **tasks:** correct command name for copilot-agent-util in task definitions ([dafe353](https://github.com/jdfalk/gcommon/commit/dafe35321f6a2584073dda612fea192c8d8c4f63))
- update applyTo patterns in instruction files for proper matching ([9942dd9](https://github.com/jdfalk/gcommon/commit/9942dd9f36a7e9aeb18c3e07862df4b1bf7953d5))
- update file permissions for workflow fix pipeline script ([3543562](https://github.com/jdfalk/gcommon/commit/35435629eab596ac790820d5d0848d2c52e586f2))
- update file permissions for workflow fixer script ([a0bdbf4](https://github.com/jdfalk/gcommon/commit/a0bdbf490965851419e71ac1300bda0bcafbef02))
- update go_package option in proto files to use the correct path ([5f4b6cf](https://github.com/jdfalk/gcommon/commit/5f4b6cfc741a92eb8c3ce5db96436f17c1abbc6f))
- update health status imports and message types to use metrics package ([2ebe0c3](https://github.com/jdfalk/gcommon/commit/2ebe0c358fad0306e1aefd4ba6ec9a387dca4bf7))
- update import path for health status and correct message type reference ([3f710a5](https://github.com/jdfalk/gcommon/commit/3f710a53320e2f0dbfd9d8dfbe4b5c9ead2d821d))
- update import paths and message types to use metrics package ([379e370](https://github.com/jdfalk/gcommon/commit/379e370e78d11614177738bc2e18c929289449cc))
- update import paths and rename RPC request/response types in proto files ([616bc1d](https://github.com/jdfalk/gcommon/commit/616bc1dc314bcd1e6cd6fd0219f0e1a501338731))
- update import paths for health status in health proto files ([dba4f37](https://github.com/jdfalk/gcommon/commit/dba4f3745858942ad241da00d580a8c7f11d0769))
- update import paths for MFA proto files to use fully qualified paths ([e87adcd](https://github.com/jdfalk/gcommon/commit/e87adcd3a67c990a423276b2f336340c03f2f0ec))
- update import paths for proto files to use fully qualified paths ([7d8706f](https://github.com/jdfalk/gcommon/commit/7d8706f1f2a5c548ab71b88a298163b2ef05bc40))
- update ListSubscriptionsResponse to use fully qualified type for subscriptions ([deac7b0](https://github.com/jdfalk/gcommon/commit/deac7b00bb755682237f0666b52ae38f0129cce1))
- update markdownlint configuration for line length and add specific rules for CHANGELOG.md and AGENTS.md ([7d0d1d9](https://github.com/jdfalk/gcommon/commit/7d0d1d9f59cffebdb62dfbf02c745fd54639813d))
- update PR automation permissions and add AI rebase ([79fa99b](https://github.com/jdfalk/gcommon/commit/79fa99baba58edc868537c29961bcca48fa99d15))
- update Prettier configuration to increase print width for markdown files ([10096cb](https://github.com/jdfalk/gcommon/commit/10096cbde0d52fb36b9148fc94c635824b6fb5c5))
- update proto files to use edition instead of syntax ([2dca9a5](https://github.com/jdfalk/gcommon/commit/2dca9a51585b858278040835ef1a8e4b964618e8))
- update protobuf definitions ([bc258e3](https://github.com/jdfalk/gcommon/commit/bc258e36712ea2e313dc8f32bb182277145d1f3d))
- update protobuf definitions ([8c2b589](https://github.com/jdfalk/gcommon/commit/8c2b589fca1ee54ce4607ad53ca7b1806a5a830d))
- update protobuf definitions ([535474a](https://github.com/jdfalk/gcommon/commit/535474abe612fb6c8f4e39c8bf24a4aa62dc087d))
- update security workflow and middleware tests ([85ef2c7](https://github.com/jdfalk/gcommon/commit/85ef2c7500f3d1df6996443cba68e03120b72191))

### Documentation

- update documentation with major protobuf implementation milestone ([47ca62d](https://github.com/jdfalk/gcommon/commit/47ca62dca106f19a394e4952698c20a84c9d0186))

### Features

- Add API_OPAQUE option to protobuf files. ([82c8d04](https://github.com/jdfalk/gcommon/commit/82c8d04428b0d52f43d6f836285ae2efc0d386a2))
- add auth and cache examples ([60aa67c](https://github.com/jdfalk/gcommon/commit/60aa67ca7d5afdba5dd6091c43d07b11634c3983))
- add Buf lint tasks for improved code quality checks ([339b59d](https://github.com/jdfalk/gcommon/commit/339b59d0da13b6b0631d93918cadcf0b31f4e578))
- Add CodeQL configuration for security analysis ([00f301f](https://github.com/jdfalk/gcommon/commit/00f301f774a3ee46f8e8f15d72d7bdc3b7cc566c))
- add comprehensive issue system monitoring and repair ([5cc49a2](https://github.com/jdfalk/gcommon/commit/5cc49a2cce9ccfb8a3b9b5a27048b813a65e577e))
- Add comprehensive tasks for gcommon implementation ([5cb5650](https://github.com/jdfalk/gcommon/commit/5cb5650e411527744119d5baf89e0a8af3b35098))
- add ConfigService with gRPC support ([d4a45ec](https://github.com/jdfalk/gcommon/commit/d4a45ec1283f8e65be43b95b41fe3207e1b40e5c))
- add consolidated PR automation workflow with code quality checks and conflict resolution ([ad3af3b](https://github.com/jdfalk/gcommon/commit/ad3af3bdffd7d54e1b7084b8b56f56f56a9abd8d))
- Add database proto definitions for connection info, migration, and transaction management ([94eb39a](https://github.com/jdfalk/gcommon/commit/94eb39aeefc08aa8d390a8d17b9da0b34bcedf94))
- add dry-run option for deployment script to preview actions without executing ([0d63363](https://github.com/jdfalk/gcommon/commit/0d63363e214ddddb2d849d52e03584d31a768480))
- Add error.proto mapping to buf.gen.yaml ([c35b554](https://github.com/jdfalk/gcommon/commit/c35b5545af7c99b95ec6bef397250b6924573b25))
- Add generated Go code for auth module ([a888d3a](https://github.com/jdfalk/gcommon/commit/a888d3ab259f25e6e5a794091b4485a14e36e65a))
- Add generated golang code for auth module. ([75c7286](https://github.com/jdfalk/gcommon/commit/75c7286c6565e74373a0344bee88112083286654))
- Add generated python code for auth module. ([d94af67](https://github.com/jdfalk/gcommon/commit/d94af67d5c4da440000ba184a4f1138cfcf86c2c))
- Add GetRoleResponse and DatabaseStatus with corresponding enums ([c1702c7](https://github.com/jdfalk/gcommon/commit/c1702c7707f79782a884d1c20a3887808d99b3ee))
- add GitHub Workflow Health Monitor for continuous monitoring and alerting ([eb10161](https://github.com/jdfalk/gcommon/commit/eb1016164ebd8ca63a3d3e1d4837aa5065a673e7))
- add gRPC service for cache operations ([bf2922c](https://github.com/jdfalk/gcommon/commit/bf2922c628cfb67e43e4653ed78a5fe8b2bbe430))
- add HTTP metrics middleware tests and remove obsolete proto files ([a49d422](https://github.com/jdfalk/gcommon/commit/a49d422116e531e669044ab476457e0574534386))
- add HttpHeader and MimeType message definitions with builders ([39df882](https://github.com/jdfalk/gcommon/commit/39df88243996542038502785a7723eec958e17b0))
- add HttpHeader, MimeType, and UrlPath proto definitions ([6caf2a7](https://github.com/jdfalk/gcommon/commit/6caf2a7b987b8373d1834c3426953ef96ec26c72))
- add label management functionality to WorkflowFixer ([db35fd2](https://github.com/jdfalk/gcommon/commit/db35fd2a40710d417ecba70f68b86d98e4d7a5c6))
- add missing common type imports and fix config entry ([c99a146](https://github.com/jdfalk/gcommon/commit/c99a146679962c4686d7fe1f28900e7085975959))
- Add mock implementation for CacheServiceServer using mockery ([ba3a0d4](https://github.com/jdfalk/gcommon/commit/ba3a0d4f74747836f8214ace3eaa591de878d8b5))
- Add mock implementation for HealthServiceServer using mockery ([c729004](https://github.com/jdfalk/gcommon/commit/c7290041c78c218b750993757ca8318713639054))
- Add mock implementation for SessionServiceServer ([17a353d](https://github.com/jdfalk/gcommon/commit/17a353d4e1a353787dfae958983f44deabf45900))
- Add mock implementations for QueueAdminService and WebAdminService ([24a0b96](https://github.com/jdfalk/gcommon/commit/24a0b960b3c3a12eadff8c8f6db579aeed6f2f96))
- Add new proto imports for consistency across health module files ([b3524fe](https://github.com/jdfalk/gcommon/commit/b3524fe0395b704cb3cc0ea9b16d87cbe75393ae))
- Add new proto imports for consistency across log module files ([5da7a8f](https://github.com/jdfalk/gcommon/commit/5da7a8f8ce2f8f3ab1067ed705b9e4b31d33e912))
- Add new proto imports for consistency across media files ([de3fd0f](https://github.com/jdfalk/gcommon/commit/de3fd0fd867a39d0752662d6e9fa63ba4a2b01cf))
- Add new proto imports for consistency across multiple files ([9c97aa8](https://github.com/jdfalk/gcommon/commit/9c97aa825234eea532a3c52ec6b25ba4ad07c032))
- Add new proto imports for consistency across notification proto files ([0ac6e09](https://github.com/jdfalk/gcommon/commit/0ac6e09c5dbbeb62abd5318290498614e82096e8))
- Add new proto imports for consistency across organization proto files ([ba96d41](https://github.com/jdfalk/gcommon/commit/ba96d410721755639c657df5e74e11c5ff16d230))
- Add new proto imports for consistency across various proto files ([628e078](https://github.com/jdfalk/gcommon/commit/628e0789edc02e0d1812b6b5b51fa4c440df7abd))
- Add new proto imports for enhanced cache service functionality ([6c182b3](https://github.com/jdfalk/gcommon/commit/6c182b3125dcc422b97c190d503d6fbd8c8978c2))
- add organization and config imports to resolve missing types ([3c3846e](https://github.com/jdfalk/gcommon/commit/3c3846e945b8e9eda97f101d0ff7d12062fd1866))
- add pagination_options.proto for standard paging parameters ([6bc2a3b](https://github.com/jdfalk/gcommon/commit/6bc2a3bb1be15592c7514f5407272393bdbe622f))
- add PR automation workflow with unified automation, code quality checks, and intelligent labeling ([290688e](https://github.com/jdfalk/gcommon/commit/290688e22fa2cb6774c8cf0d0c51d7650e81b8cc))
- Add proto definitions for circuit breaker, error handling, and subscription management ([b0f42d2](https://github.com/jdfalk/gcommon/commit/b0f42d2272f4ee428fce680f96b4faa516721422))
- Add proto definitions for organization management ([304d226](https://github.com/jdfalk/gcommon/commit/304d226011eb1ca9909f46449b484a9650f42467))
- add protobuf definitions for logger configuration and management services ([bf956be](https://github.com/jdfalk/gcommon/commit/bf956beab56c9be143b61a996b2362e43b704b5d))
- Add protobuf responses for cache operations ([324a8a7](https://github.com/jdfalk/gcommon/commit/324a8a76e58225a3f5e9a0ca2eb39be2f5b09bf8))
- Add recovery handling in metrics tests to prevent panics ([2a7843b](https://github.com/jdfalk/gcommon/commit/2a7843b54b37d86169f5c4e47ee763c6b0d04cf4))
- add repository audit script for file consistency and version checks ([ee0da9f](https://github.com/jdfalk/gcommon/commit/ee0da9f42b0b33d043838cfbd2d4e48b305ca591))
- Add response types for metrics operations ([433251d](https://github.com/jdfalk/gcommon/commit/433251d0c3dc63107081a8d7bb09ba6fcd0f2c58))
- Add retention policy, validation config, and subscription config messages ([5397671](https://github.com/jdfalk/gcommon/commit/539767101d5d80cb3f996ae06c55a9c147aad521))
- add RetentionPolicy enum for metrics data retention options ([a6860f6](https://github.com/jdfalk/gcommon/commit/a6860f6025ec64a8465325077a5f66e9f51e7c58))
- add reusable Super Linter workflow configuration ([6277084](https://github.com/jdfalk/gcommon/commit/627708422761ce74ea4ada28b77195e907f13353))
- add Rust coding style guide and best practices documentation ([a3271d0](https://github.com/jdfalk/gcommon/commit/a3271d0ca74f88aeb3c02832e1b72348e5ec11d4))
- add scripts for resolving proto file conflicts and duplicates ([b4755bc](https://github.com/jdfalk/gcommon/commit/b4755bc5e3e87b8ff2feb730a7c930823dc858e2))
- add scripts to find and process conflicted PRs with automated comments ([a6e576d](https://github.com/jdfalk/gcommon/commit/a6e576daed5e846ff7b65bab64dd20a5ff24f3fb))
- add scripts to fix missing type imports in protobuf files ([2f0abaa](https://github.com/jdfalk/gcommon/commit/2f0abaa3e2052df228d0283f941a08ee2df7560a))
- add subscription management proto definitions ([3e3de76](https://github.com/jdfalk/gcommon/commit/3e3de76ec2cb0c6b41c7011159b0ddec7867835f))
- add SubscriptionInfo and SubscriptionOptions proto messages ([25121fa](https://github.com/jdfalk/gcommon/commit/25121fab6cdde6510e56bdbbb3323ab597a31e16))
- add task for Buf Generate Per Module in VSCode ([1fb1313](https://github.com/jdfalk/gcommon/commit/1fb131374573db1cc878f0cd0b12a491bd1093aa))
- add TenantService gRPC and Proto definitions ([c980a12](https://github.com/jdfalk/gcommon/commit/c980a12a6a668e9c41b43479988f1737e7151813))
- add version update guidelines to AGENTS.md ([1e1cdc3](https://github.com/jdfalk/gcommon/commit/1e1cdc39c6ac84c128d733d7f8da484d56bb3098))
- add VS Code tasks guidance to general coding instructions ([61d8472](https://github.com/jdfalk/gcommon/commit/61d8472f4d4b5564f96a05466ca6757674317d3e))
- add WebAdminService and WebService proto definitions ([4811ee2](https://github.com/jdfalk/gcommon/commit/4811ee2ad5a06cfd25020a6566b9b27ba8969520))
- add WebService proto definition for handling HTTP requests and health checks ([265100b](https://github.com/jdfalk/gcommon/commit/265100b6d2103f0c264a68cd0f85d350e4265130))
- add workflow consolidation in progress ([7651aeb](https://github.com/jdfalk/gcommon/commit/7651aeb79836a6618a4cb545ef9e8b5f9a835435))
- add workflow management service with start and stop workflow requests and responses ([28b6976](https://github.com/jdfalk/gcommon/commit/28b6976159ab832c9024c92fd622b4c82c0684dc))
- Add WorkflowService proto for workflow management operations ([a1568ee](https://github.com/jdfalk/gcommon/commit/a1568eeaae3c5f7be10cf3372049eba34fe2a0e0))
- **analyzer:** enhance summary output with organized issue breakdown for better clarity ([7af55a0](https://github.com/jdfalk/gcommon/commit/7af55a07d929bf19968d14249516b35d6a34e193))
- **auth:** Add auth proto. ([142f314](https://github.com/jdfalk/gcommon/commit/142f314a8331939be408be8fe19770fae3100c07))
- **auth:** add AuthorizationService and SessionService proto definitions ([49a6bbb](https://github.com/jdfalk/gcommon/commit/49a6bbb9653b1bcb22160bf0de63b81a400a013d))
- **auth:** add missing protobuf definitions ([76a9f74](https://github.com/jdfalk/gcommon/commit/76a9f74254a55054570ec149f51b489af29a1afc))
- **auth:** add OAuth2 and LDAP providers with token revocation ([6dba339](https://github.com/jdfalk/gcommon/commit/6dba339aa9a6526fb555ce3a399f20cf84ba5655))
- **auth:** add proto definitions for audit events, refresh tokens, and security policies ([825afa1](https://github.com/jdfalk/gcommon/commit/825afa14092baf67465e2e2c8593f0999a48b620))
- **auth:** Add protobuf definitions for session and token management ([a138c2d](https://github.com/jdfalk/gcommon/commit/a138c2df857f9176e0d5e383cb74f71f713bd06c))
- **auth:** add security context and policy proto definitions ([52f5c65](https://github.com/jdfalk/gcommon/commit/52f5c65377c50a8f46157d76ece7da2248de7a82))
- **auth:** complete auth module services and policies ([1f5754b](https://github.com/jdfalk/gcommon/commit/1f5754bcd14888cc97b1b939fa5d1fdf07968252))
- **auth:** implement auth module protobuf definitions ([e041f30](https://github.com/jdfalk/gcommon/commit/e041f3086269dd04f04d4cc3a18d23eae330bf2e))
- **automation:** comprehensive fix for issue management workflow problems ([01e1336](https://github.com/jdfalk/gcommon/commit/01e13364ce0e95e9c5113e384736bf6eb05940d9))
- **buf:** scaffold multi-language SDK generation ([c58b424](https://github.com/jdfalk/gcommon/commit/c58b4240c986aa2dfd955e0bf89190a3f04bfccf))
- **build:** Add per-module protobuf generation and import fixing utilities ([c8cdb33](https://github.com/jdfalk/gcommon/commit/c8cdb3353362d2ce4204cf41ab5bf74255b71f87))
- **cache:** Add go generated files ([032ae95](https://github.com/jdfalk/gcommon/commit/032ae956aaa0ba68c9764175a9b6164b59531108))
- **cache:** add memcached provider and batch operations ([4955aed](https://github.com/jdfalk/gcommon/commit/4955aed230704fd57ac37f7c6d6bc6b79cbf553f))
- **cache:** add proto definitions for cache management requests and responses ([1c369af](https://github.com/jdfalk/gcommon/commit/1c369af49f3387b64449c880f235bba99bdfca17))
- **cache:** implement full cache module ([2827230](https://github.com/jdfalk/gcommon/commit/2827230b49e13fc66ab758d92aa0365180ddd976))
- **cache:** update protobuf file headers and editions ([1a9e1cd](https://github.com/jdfalk/gcommon/commit/1a9e1cd4174f51f942354fbfa2466ce4600c9ba2))
- **ci:** add environment deployment steps ([2554255](https://github.com/jdfalk/gcommon/commit/2554255d0bca31e5f9302e46c882df79607463f8))
- **ci:** scaffold pipeline infrastructure for quality gates ([#64](https://github.com/jdfalk/gcommon/issues/64)) ([b950021](https://github.com/jdfalk/gcommon/commit/b9500213b8f68992daa2815ee9616e3941c522d8))
- **codegen:** Add complete Go protobuf generated files for all modules ([58279ef](https://github.com/jdfalk/gcommon/commit/58279effbb1c3c14f17756f3f7cbb0947e1451ad))
- **codegen:** Update Python protobuf generated files with import fixes ([cea7df1](https://github.com/jdfalk/gcommon/commit/cea7df1016cabbd34e6467738629f078bc682fbb))
- **common:** Add go generated files ([1b13f24](https://github.com/jdfalk/gcommon/commit/1b13f249ad9f5e7cecb14ebd2e45e70ce6959e23))
- **common:** implement sorting functionality types ([27b70e6](https://github.com/jdfalk/gcommon/commit/27b70e6c88ba01c6e584ceb6986bb2604dcdce0b))
- **common:** update protobuf file headers and editions ([92a8e5e](https://github.com/jdfalk/gcommon/commit/92a8e5e7cba474ff0135b7d70011d019213ee20f))
- complete Phase 3 - specialized workflows and enhanced release automation ([2e5fbcd](https://github.com/jdfalk/gcommon/commit/2e5fbcd4abcd60e27c6524a8beb2576c86c2de49))
- complete synchronization infrastructure for consolidated workflows ([d5bd165](https://github.com/jdfalk/gcommon/commit/d5bd165e2b8ccb4fefe3cc5529e945e8baca7723))
- comprehensive protobuf fixes and generation improvements ([3c6d6f6](https://github.com/jdfalk/gcommon/commit/3c6d6f6493df9272cc80135681e501a2cbb5fa7c))
- **config:** add config module service skeleton ([6aba560](https://github.com/jdfalk/gcommon/commit/6aba5603cb081d7fdeefbcedab025c7e1262eed8))
- **config:** add foundational enum types for configuration system ([7619862](https://github.com/jdfalk/gcommon/commit/7619862f867aa690fd98076f5c7a2484b8bdd3fa))
- **config:** Add go generated files ([b69b3d0](https://github.com/jdfalk/gcommon/commit/b69b3d06de8c08cad4611fea5d415f62e411b68e))
- **config:** Add Prettier and YAML linting configuration files ([e3f4d68](https://github.com/jdfalk/gcommon/commit/e3f4d68b4eb44e9f8f814592cdde39c94fe73d5e))
- **config:** Add protobuf definitions for configuration management ([8e8e8ea](https://github.com/jdfalk/gcommon/commit/8e8e8eaff2451e6018e396adb109d21349514b56))
- **config:** add provider factory and basic providers ([8f2cfa0](https://github.com/jdfalk/gcommon/commit/8f2cfa067f8781623a6913b22f8a123e94211eec))
- **config:** enhance configuration management with TOML and auto detection ([#24](https://github.com/jdfalk/gcommon/issues/24)) ([6bdcc9e](https://github.com/jdfalk/gcommon/commit/6bdcc9ea685d62fdb8ea66298e3cc40f27f772cc))
- **config:** expand configuration management system ([#24](https://github.com/jdfalk/gcommon/issues/24)) ([48cbd00](https://github.com/jdfalk/gcommon/commit/48cbd005f6c597cdedefcab29f0d264c416fc334))
- **config:** implement configuration enums and metadata types ([fb84d3a](https://github.com/jdfalk/gcommon/commit/fb84d3a00e0ffbcf648727fa0caceb7a00530d87))
- **config:** split large proto files following 1-1-1 pattern ([f50e967](https://github.com/jdfalk/gcommon/commit/f50e9674331aec9c66bfbda5bcbe56a39efa49c0))
- **config:** update protobuf file headers and editions ([aa4cb9d](https://github.com/jdfalk/gcommon/commit/aa4cb9dc61b851613320398ad4587961aeb57f6a))
- **db:** add DatabaseStatus proto ([983d98d](https://github.com/jdfalk/gcommon/commit/983d98d76c1bb663913b3463dfac166df653550d))
- **db:** Add go generated files ([09f5016](https://github.com/jdfalk/gcommon/commit/09f501685cdff71ecaefd04cf255ebda3cfa92ef))
- **db:** add MigrationService gRPC ([ee31b49](https://github.com/jdfalk/gcommon/commit/ee31b4982feef1a2a65fb0027413817fecb6c292))
- **db:** implement comprehensive migration system ([ea0070c](https://github.com/jdfalk/gcommon/commit/ea0070c7a0793c9a57dfd378c21d7ca4414958e2))
- **db:** update protobuf file headers and editions ([aa064c3](https://github.com/jdfalk/gcommon/commit/aa064c3f80ff1f12e2c7cf7925be55336be41bc3))
- **deploy:** add deployment templates and monitoring config ([ad05d1c](https://github.com/jdfalk/gcommon/commit/ad05d1c859b6aa3960d6de478af4998e86291af9))
- **deploy:** expand containerization stack ([a63bb2a](https://github.com/jdfalk/gcommon/commit/a63bb2a97e902226290e5c377ea20f475e37836a))
- **deps:** enhance dependency audit ([cce086f](https://github.com/jdfalk/gcommon/commit/cce086f751c3b07c717e804d91dddb1d90615852))
- **docs:** add API documentation generator ([665d92d](https://github.com/jdfalk/gcommon/commit/665d92d75e5032da44cc0777acc57b0c9845b973))
- **docs:** Update CLAUDE.md and copilot-instructions.md for improved clarity; add repository setup, review selection, workflow usage, and security guidelines documentation ([82e0111](https://github.com/jdfalk/gcommon/commit/82e011110402e7ce11c703ef076eda481f445503))
- enhance documentation for copilot-agent-util with arguments file support ([9366cee](https://github.com/jdfalk/gcommon/commit/9366ceea9fc1de2ba60c7fa45f5ace0eabc06755))
- **errors:** standardize error handling across modules ([22745af](https://github.com/jdfalk/gcommon/commit/22745af8b8be85ad64534fa1cdd73da37308ba62))
- **examples:** add initial tutorials for core modules ([083880c](https://github.com/jdfalk/gcommon/commit/083880c1329e7db1318a346b908eccef4838c02e))
- **examples:** scaffold Go example skeletons ([503dfc0](https://github.com/jdfalk/gcommon/commit/503dfc0169668f995a4fb0c4b79e2295df515fb2))
- fix protobuf compilation errors - batch 1 ([e75113e](https://github.com/jdfalk/gcommon/commit/e75113efffa5a8c957e35baa7e582a18493bfac9))
- **github:** setup complete GitHub automation and structure ([61e6666](https://github.com/jdfalk/gcommon/commit/61e6666f86d1e4e471e30b4c768e33cf4c6ff2a1))
- **grpc:** add advanced client resilience features ([ab2b583](https://github.com/jdfalk/gcommon/commit/ab2b5838aa29ec5cf6b43b8d91937343a1af303e))
- **grpc:** add resilience utilities for gRPC client ([#882](https://github.com/jdfalk/gcommon/issues/882)) ([541a2ef](https://github.com/jdfalk/gcommon/commit/541a2efa88b494ba9cce318b78ab0f3d2f1eb5c9))
- **health:** update protobuf file headers and editions ([883a43b](https://github.com/jdfalk/gcommon/commit/883a43b46e32be2c88eb7fcb500e6910aa017ba3))
- Implement ListTenantsRequest and RemoveMemberRequest with pagination and filtering ([2b1ce64](https://github.com/jdfalk/gcommon/commit/2b1ce64df8fd34fe18179925aadaa4b3e61c980b))
- implement QueueService with core queue operations ([e0381d3](https://github.com/jdfalk/gcommon/commit/e0381d330150ffdd79da49be5e539e43ec773cd5))
- Implement UpdateTenantQuotaResponse with quota field and related methods ([f3b555a](https://github.com/jdfalk/gcommon/commit/f3b555aebdf2a0fb559afdee1d07f582910284c5))
- integrate AI rebase functionality into consolidated PR automation workflow ([3aa04c3](https://github.com/jdfalk/gcommon/commit/3aa04c3323bdf450b894f98b12dbccf9ca54ebd9))
- Introduce integrated GitHub Workflow Fixer script ([6d13ab3](https://github.com/jdfalk/gcommon/commit/6d13ab39aab4b0163f57c8345f7d9c80e956aa6a))
- **lint:** implement script to fix buf lint issues by removing unused imports ([fb903be](https://github.com/jdfalk/gcommon/commit/fb903be92093ed069c1ed934049c3069dcff7e8c))
- **log:** add gRPC log service with WriteLog and ReadLogs methods ([b5fe3bd](https://github.com/jdfalk/gcommon/commit/b5fe3bdcc493de98fc8cd239bef2873ba7e738a9))
- **log:** add protobuf definitions for log operations ([c9719c9](https://github.com/jdfalk/gcommon/commit/c9719c9efd772e555425fd8bbfb2eb47991a95ba))
- **log:** Add protobuf definitions for logging configuration, entry, and statistics ([cb7fb17](https://github.com/jdfalk/gcommon/commit/cb7fb173bde4454bfd3fd97ceb746531c420c965))
- **log:** implement comprehensive logging module ([bb968df](https://github.com/jdfalk/gcommon/commit/bb968df1a43e80cbcd5309c8df339dd4bbe3e991))
- **log:** standardize module logging ([f624daf](https://github.com/jdfalk/gcommon/commit/f624daff1213c52b0a8ff646e129a693061a270c))
- **log:** start log proto migration ([73cba6c](https://github.com/jdfalk/gcommon/commit/73cba6cf19602648ecdd753943612a2f0d3d4649))
- **log:** update protobuf file headers and editions ([3bd00e1](https://github.com/jdfalk/gcommon/commit/3bd00e16b57765a740979df8b4c9f743738d5717))
- **makefile:** add target to generate protobuf files per module with detailed reporting ([20a5382](https://github.com/jdfalk/gcommon/commit/20a538228352261628989a7e07096be34cca81b7))
- massive protobuf import fixes - systematic resolution ([7225254](https://github.com/jdfalk/gcommon/commit/7225254a6f9ce1e9e5de0e3cfb28d3243419ed80))
- massive protobuf malformed import cleanup - batch 3 ([f553e61](https://github.com/jdfalk/gcommon/commit/f553e615fe5aca7151da7e3e6a54d31ac6befead))
- **media:** add initial media protobufs ([0623d2b](https://github.com/jdfalk/gcommon/commit/0623d2b1af74265d3e5cf34734eb99def2378b2b))
- **media:** Add protobuf definitions for audio track, media file, metadata, quality, type, movie info, series info, subtitle track, and resolution ([8c477e8](https://github.com/jdfalk/gcommon/commit/8c477e8e1e7adffc53f20b0773201efac648de3a))
- **media:** update protobuf file headers and editions ([3427bbd](https://github.com/jdfalk/gcommon/commit/3427bbd0ff8b1a167b816b33242baa50ccb0e6b7))
- **metrics:** Add GetMetricRequest and GetScrapeConfigRequest with metadata support ([aa70fa3](https://github.com/jdfalk/gcommon/commit/aa70fa3e1db7b9a184665f8a7b48bda079ae42eb))
- **metrics:** add gRPC service for metrics management ([0fbaeb2](https://github.com/jdfalk/gcommon/commit/0fbaeb2075c61dc5e905a5cab62174ef4d2912d1))
- **metrics:** Add protobuf definitions for metrics module ([32500fd](https://github.com/jdfalk/gcommon/commit/32500fd6a152cc4e0b1a5d3a80264db4a03cfe5c))
- **metrics:** add ResetMetricsRequest and related functionality ([2418215](https://github.com/jdfalk/gcommon/commit/241821529744bc601b6bb6757b493ee559925e1d))
- **metrics:** enhance memory metrics provider ([c2e3db9](https://github.com/jdfalk/gcommon/commit/c2e3db9d949e18e79abf5b7d438f40c4125bf300))
- **metrics:** implement metrics provider and registration types ([b4f40ac](https://github.com/jdfalk/gcommon/commit/b4f40ac9fddc38519dc02c641dd9c3d8c5a25609))
- **metrics:** implement request and response protos ([c9f885f](https://github.com/jdfalk/gcommon/commit/c9f885f77847add78600779e3089c4ed49232642))
- **metrics:** implement request and response protos ([0515166](https://github.com/jdfalk/gcommon/commit/05151669f39c8285639e476d9620b42348a6368c))
- **metrics:** implement request and response protos ([a7a0957](https://github.com/jdfalk/gcommon/commit/a7a0957f903d04854ceb54684df606f703ab82fd))
- **metrics:** split large proto files following 1-1-1 pattern ([381a850](https://github.com/jdfalk/gcommon/commit/381a8507e0742acc1ed74333790de0c1d8917f87))
- **metrics:** update protobuf file headers and editions ([0e4c57d](https://github.com/jdfalk/gcommon/commit/0e4c57d2a6488506086b49b53b9277c8ad6f8057))
- **monitoring:** expand observability infrastructure ([a378427](https://github.com/jdfalk/gcommon/commit/a37842762fd9ee544c3a8d2f9da988ec4493cd5f))
- **network:** add additional egress ranges ([f420a90](https://github.com/jdfalk/gcommon/commit/f420a903863f3c93b4b1dad7213be5b7f2930584))
- **notification:** add MarkAsReadResponse proto and service methods ([607158c](https://github.com/jdfalk/gcommon/commit/607158c8d3a947bf9e6e56c75d08efae13dfbbbd))
- **notification:** Add protobuf definitions for notification management including requests and responses ([9a1991e](https://github.com/jdfalk/gcommon/commit/9a1991e5766814f4721e531124fd4d3c086cd53b))
- **notification:** add read and delete protobufs ([0ac32a1](https://github.com/jdfalk/gcommon/commit/0ac32a1d79b2dcb6aa5a37f1018680ef8d1dea93))
- **notification:** add UpdatePreferencesResponse and NotificationService ([f1dd089](https://github.com/jdfalk/gcommon/commit/f1dd08927dc3feace504ed8b1e95abf1deb98986))
- **notification:** implement core notification module ([3b1ef5c](https://github.com/jdfalk/gcommon/commit/3b1ef5ccae93a8f47ca6b5428b748d3b7dd83fac))
- **notification:** implement service layer and tests ([9344f30](https://github.com/jdfalk/gcommon/commit/9344f308e3cd3dfdb6cf935e742cde14242497bb))
- **notification:** update protobuf file headers and editions ([02b7749](https://github.com/jdfalk/gcommon/commit/02b774995a69916808ad3692e614dc7af7801dcd))
- **organization:** add organization service layer ([90b2e90](https://github.com/jdfalk/gcommon/commit/90b2e90414be7965c2dde756f6689ebb3a2c955b))
- **organization:** add TenantQuota proto definition ([6395955](https://github.com/jdfalk/gcommon/commit/63959555d10272305f807449016b9b2804429cbb))
- **organization:** scaffold multi-tenant service layer ([6ac9932](https://github.com/jdfalk/gcommon/commit/6ac9932577de5aec2ad1a298695d44b931c9f8c4))
- **organization:** update protobuf file headers and editions ([0eeae43](https://github.com/jdfalk/gcommon/commit/0eeae4312e228015bf860c24a7b9a3de31acaca8))
- **perf:** add performance testing framework ([f497823](https://github.com/jdfalk/gcommon/commit/f497823ff94a21f9bc9c4138ca09becf69ff9ba6))
- **perf:** expand performance testing framework skeleton ([87d1e35](https://github.com/jdfalk/gcommon/commit/87d1e3597a20cb3b7444d2067e26365cf2bd74bd))
- **prompts:** Add various AI prompt templates for documentation, code review, and issue management ([4847a6b](https://github.com/jdfalk/gcommon/commit/4847a6b399c7c347f95ddedd7742cac0adc7e19a))
- **proto:** add 1-1-1 pattern splitting infrastructure ([ad1f89a](https://github.com/jdfalk/gcommon/commit/ad1f89aa0b00420fcd0e731181422ba6a08c70e8))
- **proto:** Add ArchiveCriteria message for log file archiving rules ([d07c0f2](https://github.com/jdfalk/gcommon/commit/d07c0f2cdfbbc6b6eee010a71e038132a8efc79b))
- **proto:** Add comprehensive analysis tool for protocol buffer files ([959aa53](https://github.com/jdfalk/gcommon/commit/959aa5322a93556fa859bcd111df7fdbcac1c3d6))
- **proto:** add ConfigChangeType enum for configuration change events ([c67fb3b](https://github.com/jdfalk/gcommon/commit/c67fb3b141d865535c67ffe2fd1130e1db0d18d0))
- **proto:** add enums for database consistency, status, and isolation levels ([9279302](https://github.com/jdfalk/gcommon/commit/9279302d0c6a8a6631a2f56b84af40bc06d843e1))
- **proto:** add formatter and output config protobuf definitions; update log service imports ([4e2a84a](https://github.com/jdfalk/gcommon/commit/4e2a84abb5406a5bda1345bbff42032e58316b45))
- **proto:** add generated gRPC service for WebService with HandleRequest and HealthCheck methods ([3b085ef](https://github.com/jdfalk/gcommon/commit/3b085ef401c853b681b71e150d2fd3c547fba53b))
- **proto:** add new protobuf definitions for appender, output, and formatter configurations ([58c8990](https://github.com/jdfalk/gcommon/commit/58c8990da53eaa391bc33e2ec4b1a2310fef6b3a))
- **proto:** add new protobuf definitions for approval stages, workflows, backup policies, and configuration management ([f5982d9](https://github.com/jdfalk/gcommon/commit/f5982d9c66d0bc46c64247a04a273be56b5de6b2))
- **proto:** add new protobuf definitions for authentication and authorization services ([f5189c0](https://github.com/jdfalk/gcommon/commit/f5189c0769ead1925a20ceeeb8626398e3f9e2d2))
- **proto:** add new protobuf definitions for component health and health check result ([73d28f0](https://github.com/jdfalk/gcommon/commit/73d28f0953633c1096c63e35cf4ddac0c0af4694))
- **proto:** add new protobuf definitions for namespace statistics and responses ([d326425](https://github.com/jdfalk/gcommon/commit/d3264258c21f68ccbe2b1527f5b7887cc1edcb7d))
- **proto:** add new protobuf definitions for pagination, rate limiting, and response metadata ([80810c6](https://github.com/jdfalk/gcommon/commit/80810c61f8ed47459e0dc37a9e7f6c53fbabd023))
- **proto:** add protobuf and gRPC definitions for log management services ([006bcd3](https://github.com/jdfalk/gcommon/commit/006bcd312824b949667419b3fc5863e014a7c1d9))
- **proto:** add script for automatic protobuf conflict resolution ([13534fb](https://github.com/jdfalk/gcommon/commit/13534fb86c7a98f79948ef8a3dbbf438a9285e17))
- **proto:** add script to reorganize proto files for Go code generation ([c9432c4](https://github.com/jdfalk/gcommon/commit/c9432c469029796fe17de8fe0b467e92d2b742e4))
- **proto:** add skeleton files for various request and response messages with compilation disabled ([d1096e0](https://github.com/jdfalk/gcommon/commit/d1096e0e53ee0d6c935105dfb2dfb2b78ee8e2c0))
- **protobuf:** add generated enum and type definitions ([65ef099](https://github.com/jdfalk/gcommon/commit/65ef099e2c60e08fe372091aa4cbdb77d306d2ee))
- **protobuf:** add generated message, request, response and service definitions ([5c7c7c3](https://github.com/jdfalk/gcommon/commit/5c7c7c3d4306d079fb27515ebe8ca112d01cf8a1))
- **protobuf:** generate Go bindings for cache, notification, and organization modules ([234e64c](https://github.com/jdfalk/gcommon/commit/234e64c54e6ce736b5a173f59623b1855c2f73d1))
- **protobuf:** generate metrics service Go protobuf files ([9f4acc5](https://github.com/jdfalk/gcommon/commit/9f4acc5eaf5cc06963ecccfdca1c864c6cf6bb6d))
- **protobuf:** generate missing protobuf Go bindings ([db96dfb](https://github.com/jdfalk/gcommon/commit/db96dfbe0bf80eaf83c34e619fbc190e5568c0b9))
- **proto:** disable conflicting definitions in WebAdminService ([c09596e](https://github.com/jdfalk/gcommon/commit/c09596e35b5cb94567f3ecfc6acc0cd6652e3cb9))
- **proto:** disable conflicting message definitions for metrics export and aggregation ([bf84da9](https://github.com/jdfalk/gcommon/commit/bf84da944e8b8f979c0a4c4cf880996fa8951a0c))
- **proto:** exclude protobuf*backup*\* from module path ([0cc058f](https://github.com/jdfalk/gcommon/commit/0cc058f1146f60562dfaf68c9cc1104e5c1b39c1))
- **proto:** implement organization request/response messages ([1f67d71](https://github.com/jdfalk/gcommon/commit/1f67d713a044839db1bf0d54afc000df7df63e74))
- **proto:** implement organization request/response messages ([e557fa2](https://github.com/jdfalk/gcommon/commit/e557fa2f4d02f533418ba094d55174f8e73b3747))
- **proto:** implement proto file naming standards checker ([1297b98](https://github.com/jdfalk/gcommon/commit/1297b98ae19d354dcf1bb1b76c43bbff33a03803))
- **proto:** remove obsolete queue and HTTP gateway service proto files ([b3d86b7](https://github.com/jdfalk/gcommon/commit/b3d86b7e2eafb81407e4770dfcb0ce3d0f604256))
- **queue:** add config protobufs and enums ([7574fa2](https://github.com/jdfalk/gcommon/commit/7574fa20f33db4e2b77f28756b4551c112862c7a))
- **queue:** Add enums for PriorityLevel, QueueType, RoutingStrategy, and SubscriptionState ([38d54fd](https://github.com/jdfalk/gcommon/commit/38d54fdc850527678c2afdf2547b715f685d5228))
- **queue:** add initial queue service layer ([bade265](https://github.com/jdfalk/gcommon/commit/bade26530903401f8114a948d171063b91177b55))
- **queue:** add proto files for subscription and topic config responses ([82dc109](https://github.com/jdfalk/gcommon/commit/82dc10937e5e363a6dade42a5dfb4c8f7b757ca6))
- **queue:** add protobuf definitions for queue module ([c62edeb](https://github.com/jdfalk/gcommon/commit/c62edeb4adec680e257931364fa67fbda06fd398))
- **queue:** complete all remaining TODO protobuf implementations ([738b2f8](https://github.com/jdfalk/gcommon/commit/738b2f8d2aa151463c93f5f347de0a5175410932))
- **queue:** complete foundational config and stats types ([ac821de](https://github.com/jdfalk/gcommon/commit/ac821de7167e09a17376af90bf409f375076757a))
- **queue:** finalize queue module protobuf definitions ([a51a2de](https://github.com/jdfalk/gcommon/commit/a51a2dec89950161b9f957bb9cb19b7b53f80e88))
- **queue:** implement 5 queue protobuf definitions ([861d34c](https://github.com/jdfalk/gcommon/commit/861d34c8e8e3cd053c5b412c699062b7789e7e7c))
- **queue:** implement additional queue module protobuf definitions ([953776b](https://github.com/jdfalk/gcommon/commit/953776b20816ceb6f4309b74f7917c025371eaf7))
- **queue:** implement admin operations and service batch 9 ([063be65](https://github.com/jdfalk/gcommon/commit/063be65b22ec180ba43b3ddb96a312180aa1c2aa))
- **queue:** implement advanced configuration types ([d44144e](https://github.com/jdfalk/gcommon/commit/d44144ecb9fd8638095fba042ac2adf3ced879bd))
- **queue:** implement advanced queue operations and topic management ([ee8ccb5](https://github.com/jdfalk/gcommon/commit/ee8ccb51657ac4eacb53827ac54169750e2604c2))
- **queue:** implement batch_pull_response message ([42aff5e](https://github.com/jdfalk/gcommon/commit/42aff5e66b6f62f7ad9ad0cd85311effe4120aab))
- **queue:** implement comprehensive alerting system ([632de73](https://github.com/jdfalk/gcommon/commit/632de7312dd5cc3072b98d471d06df9490b93eec))
- **queue:** implement configuration and utility operations ([847ff88](https://github.com/jdfalk/gcommon/commit/847ff8874d1a49eee9de46f79994109f17cdc119))
- **queue:** implement core info and stats types ([4febd04](https://github.com/jdfalk/gcommon/commit/4febd04848c1c73cc94fbacc19cc896aa8df3066))
- **queue:** implement core queue message processing definitions ([e9c67ca](https://github.com/jdfalk/gcommon/commit/e9c67ca30a8d205f3ec049c39dc10a0ff862eecc))
- **queue:** implement core queue state and operation types ([872cc6e](https://github.com/jdfalk/gcommon/commit/872cc6e3aacfec4f0e5f96a2bda8dd35ac418a0d))
- **queue:** implement core request/response message types ([67eb849](https://github.com/jdfalk/gcommon/commit/67eb849672aa0b5725c129a7ba987379c7575940))
- **queue:** implement durability config and response messages ([0249c51](https://github.com/jdfalk/gcommon/commit/0249c51af45e66d03fc5c53cd8f74e940fe44068))
- **queue:** implement foundational authorization, consistency, and consumer group types ([fa58165](https://github.com/jdfalk/gcommon/commit/fa58165b1ac94d2ce5ac4a136b58d20a4e0f203f))
- **queue:** implement foundational enums and config types ([6b83c9d](https://github.com/jdfalk/gcommon/commit/6b83c9d6ce7aa541b0e4670866ace261937b1d3c))
- **queue:** implement load balancing and routing system ([43edcdc](https://github.com/jdfalk/gcommon/commit/43edcdce5544774a2b40caaf4a9104af2fab67d2))
- **queue:** implement management operation messages batch 8 ([399b50f](https://github.com/jdfalk/gcommon/commit/399b50f56da24a09d1e765759610faa8188823a2))
- **queue:** implement message configs and export functionality ([037df9c](https://github.com/jdfalk/gcommon/commit/037df9ca93ba1f004309286a3b8ee4345bfbe622))
- **queue:** implement message publishing and queue management operations ([d2bfe76](https://github.com/jdfalk/gcommon/commit/d2bfe76b7773861735c111a210c467796e164d93))
- **queue:** implement message serialization and schema system ([8d37b42](https://github.com/jdfalk/gcommon/commit/8d37b42017699c967ab8d469f1887062107a88b4))
- **queue:** implement message_metadata core type ([e1e95c4](https://github.com/jdfalk/gcommon/commit/e1e95c444b8468ef2e767759ac03aee8f716029c))
- **queue:** implement negative acknowledgment (NACK) system ([cd985a9](https://github.com/jdfalk/gcommon/commit/cd985a9bcab3c5d9718607d381f7bd4557b92e63))
- **queue:** implement queue module protobuf definitions ([405e735](https://github.com/jdfalk/gcommon/commit/405e735683dd128abbd38cf014e8bebf1857e514))
- **queue:** implement queue operations and management messages ([9351164](https://github.com/jdfalk/gcommon/commit/93511643f393b09af7549767cb3440a88658f20c))
- **queue:** implement request/response messages batch 7 ([2cd72ac](https://github.com/jdfalk/gcommon/commit/2cd72ac33fd80170e9bd587dff3054e038cbbcd3))
- **queue:** implement statistics and monitoring system ([9e1dcb7](https://github.com/jdfalk/gcommon/commit/9e1dcb7d89b73496af7224ec87ee22b3e5c5099b))
- **queue:** implement stats, config and binding messages ([afa010d](https://github.com/jdfalk/gcommon/commit/afa010d77752efd55466f670d5a797eefef501e9))
- **queue:** implement streaming and batch operation messages ([b2307a6](https://github.com/jdfalk/gcommon/commit/b2307a69f0cabe01eefe4d45a05a492e338a39b6))
- **queue:** split large proto files following 1-1-1 pattern ([5ca7c3c](https://github.com/jdfalk/gcommon/commit/5ca7c3cf4ee2210dcb9d61a8704f36257a66a114))
- **queue:** update import statements in acknowledge and enqueue request proto files ([2ab83d2](https://github.com/jdfalk/gcommon/commit/2ab83d22fac59cda708f391e27db08943c101de8))
- **queue:** update protobuf file headers and editions ([9d52ae1](https://github.com/jdfalk/gcommon/commit/9d52ae1e6cbdd3fb418a0a3fd74d59e09cba529c))
- **readme:** update protobuf milestone and module status tables for clarity ([a341c1c](https://github.com/jdfalk/gcommon/commit/a341c1c4404c4898393f9432ce923d3476aa3994))
- Refactor proto file organization and add naming standards checker ([c10627d](https://github.com/jdfalk/gcommon/commit/c10627dc49f1758a8cf5e73a6442a31f9c351e3d))
- remove ApiKey message definition from proto file ([9cde17c](https://github.com/jdfalk/gcommon/commit/9cde17cfef5c76cede9f4f13340e66237aac0b6a))
- remove duplicate messages subdirectories ([3e42763](https://github.com/jdfalk/gcommon/commit/3e42763d9eeb0246613081cc9687c6ce179d06e1))
- remove obsolete scripts for fixing proto lint and import issues ([78f5da2](https://github.com/jdfalk/gcommon/commit/78f5da241efc9e660754912ca7b95e2d7b19388f))
- Remove TODO comment for RemoveMemberResponse message implementation ([e291807](https://github.com/jdfalk/gcommon/commit/e291807c692efcb734538c166ab3d56fdd83fc00))
- replace reusable workflows with consolidated standalone workflows ([34207a4](https://github.com/jdfalk/gcommon/commit/34207a4c70e464358cb32963bfb9b0f58bc6826b))
- scaffold documentation system ([6d9a0aa](https://github.com/jdfalk/gcommon/commit/6d9a0aaf03f40ef85dbab462dfba2ac0c4bf3663))
- **scripts:** add protobuf compilation and cleanup scripts ([c34be2a](https://github.com/jdfalk/gcommon/commit/c34be2add19ea74cfadd7324b3c882906c2337ca))
- **sdks:** add python and typescript clients ([bd2cb14](https://github.com/jdfalk/gcommon/commit/bd2cb1406019145a98cf2172a7a08d52538a6e53))
- **sdks:** add SDK generation scaffolding ([78e9841](https://github.com/jdfalk/gcommon/commit/78e9841808e8588932ecf96d7a7b859738e3c1fb))
- **security:** implement comprehensive security module ([70f5c62](https://github.com/jdfalk/gcommon/commit/70f5c62edb45de7ccf82dac3a5ff6be8c01c5f7c))
- session status handoff - buf.gen.yaml protoc builtin fix pending ([eb5c7c3](https://github.com/jdfalk/gcommon/commit/eb5c7c363fc8282642eceaca83617e3817819f67))
- standardize VS Code tasks across all repos ([fdcecc6](https://github.com/jdfalk/gcommon/commit/fdcecc6c798b9235d5da129360cb45ea652f7c49))
- **templates:** add microservice scaffolding tools ([49a921a](https://github.com/jdfalk/gcommon/commit/49a921a7c8cf846c12d47c289baa03ffcb4b129e))
- **templates:** add microservice templates and generator ([7e0f981](https://github.com/jdfalk/gcommon/commit/7e0f981a34451f9e3c989f7697132821a6c3de7e))
- **test:** expand integration testing framework ([abf87f7](https://github.com/jdfalk/gcommon/commit/abf87f75bc55bb1de00105e7f2d2c1ab7d8be98c))
- **test:** scaffold integration testing framework ([3fdde64](https://github.com/jdfalk/gcommon/commit/3fdde647cf810cc907c3a604112b2e361781eb0e))
- Update commit and pull request description instructions for clarity and versioning ([79a15c4](https://github.com/jdfalk/gcommon/commit/79a15c458918a5e03ab64caf7f3fcd0a35073a5b))
- Update OTLP exporter to use otlptrace and adjust go.sum ([48c6bff](https://github.com/jdfalk/gcommon/commit/48c6bffea8f5d3e9e9cdc6a49e84fe923b81292c))
- update PR automation workflow and permissions; add backup file ([6fb3048](https://github.com/jdfalk/gcommon/commit/6fb3048d1afa95975a1ed5c648402e643cef0aed))
- Update PR automation workflow to enable validations and adjust auto-fix settings ([5358c60](https://github.com/jdfalk/gcommon/commit/5358c60c918b74b806e15b5eed07ead6fe98a680))
- Update proto files to include new imports and remove deprecated enums ([7e387ca](https://github.com/jdfalk/gcommon/commit/7e387ca5ead28a6bc5889d03a35ece70d18fabd2))
- Update RouteInfo, SessionConfig, and SessionData Protobuf messages ([1cffbc2](https://github.com/jdfalk/gcommon/commit/1cffbc2599cab72db9d41d74d958179b152cc0fc))
- update tasks to use installed copilot-agent-util command ([e14ec8a](https://github.com/jdfalk/gcommon/commit/e14ec8a964450a10743ec15580e0645b5dc9d12c))
- Update to OTLP exporter for tracing and adjust related tests ([a6058e2](https://github.com/jdfalk/gcommon/commit/a6058e2023bb5abdfccd74cd1cad47f9169dd67b))
- update VS Code tasks to use copilot-agent-util ([bdcf9f0](https://github.com/jdfalk/gcommon/commit/bdcf9f025dda04c1df19f70918673da27d767314))
- **web:** add health check config message ([c3f28d6](https://github.com/jdfalk/gcommon/commit/c3f28d652f7ca1fc6d9903dce8f7c46d89cee900))
- **web:** add redis sessions and routing ([0daef88](https://github.com/jdfalk/gcommon/commit/0daef88a8c1d0d1e2930c9092ecc9d34cdc1f47e))
- **web:** add session management protos ([e5c424e](https://github.com/jdfalk/gcommon/commit/e5c424e0da87cc111ef30f1502c1a80f59259c74))
- **web:** complete web module\n\nImplemented server factory, middleware suite (auth, cors, metrics, rate limiting, recovery), session manager with store abstraction, handlers, routing, gRPC stubs, and usage examples. Added tests for middleware, handlers, and session manager, and enabled HTTP/2 in server.\n\nFiles changed:\n- pkg/web/factory.go - create server from config\n- pkg/web/middleware/_ - add auth, cors, metrics, rate limiting, recovery middleware and tests\n- pkg/web/session/_ - add manager and store, update memory store\n- pkg/web/handlers/_ - add health, metrics, admin handlers with test\n- pkg/web/routing/_ - add simple router and matcher\n- pkg/web/grpc/_ - add gRPC server and service stubs\n- pkg/web/examples/_ - provide build-ignored examples\n- pkg/web/server.go - configure HTTP/2 support\n- go.mod - include x/net dependency\n ([9c2088e](https://github.com/jdfalk/gcommon/commit/9c2088e3bac3a0ebf3647999435ac9b916c707b1))
- **web:** implement cache protobufs ([b169825](https://github.com/jdfalk/gcommon/commit/b16982548851cb0040a646b88969c2d25404bafe))
- **web:** implement foundational message types ([e212d62](https://github.com/jdfalk/gcommon/commit/e212d620330b6a00611b0035cc46b7e176da6941))
- **web:** implement web module protobuf definitions ([21c1405](https://github.com/jdfalk/gcommon/commit/21c14051fc56e123abcbc11d67d09a040da77349))
- **web:** update protobuf file headers and editions ([00aab10](https://github.com/jdfalk/gcommon/commit/00aab10c82b50d7349f12c2627108203931a997a))

### BREAKING CHANGES

- Major documentation update reflecting massive protobuf expansion

* Update README.md with current module status (1,254+ proto files)
* Update CHANGELOG.md with August 2025 protobuf implementation milestone
* Update TODO.md with completed protobuf phase and new gRPC focus
* Reflect transition from protobuf implementation to gRPC service development
* Document 100% completion of 1-1-1 pattern across all 12 modules
* Update module completion status from partial to proto-complete

Key achievements documented:

- Config Module: 155 proto files (was 3/23, now 155/155)
- Queue Module: 216 proto files (was 2/177, now 216/216)
- Metrics Module: 172 proto files (was 2/97, now 172/172)
- Auth Module: 172 proto files (was 17/126, now 172/172)
- Web Module: 224 proto files (was 2/178, now 224/224)
- Cache Module: 72 proto files (was 8/44, now 72/72)

Next phase: gRPC service implementation with focus on compilation fixes

- **queue:** Queue protobuf file structure completely reorganized
- **metrics:** Metrics protobuf file structure completely reorganized
- **config:** Config protobuf file structure completely reorganized
- **proto:** Proto file structure completely reorganized

<!-- file: CHANGELOG.md -->
<!-- version: 1.0.1 -->
<!-- guid: 8c9d0e1f-2a3b-4c5d-6e7f-8a9b0c1d2e3f -->

# GCommon Changelog

## Table of Contents

- [[1.0.0](https://github.com/jdfalk/gcommon/compare/v0.1.1...v1.0.0) (2025-08-15)](#-1-0-0-https-github-com-jdfalk-gcommon-compare-v0-1-1-v1-0-0-2025-08-15)
  - [Bug Fixes](#bug-fixes)
  - [Documentation](#documentation)
  - [Features](#features)
  - [BREAKING CHANGES](#breaking-changes)
- [GCommon Changelog](#gcommon-changelog)
  - [Table of Contents](#table-of-contents)
    - [Added](#added)
  - [[Unreleased]](#-unreleased)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added\n- Implemented advanced gRPC client resilience with token bucket rate limiting, bulkhead concurrency control, and request hedging](#added-n-implemented-advanced-grpc-client-resilience-with-token-bucket-rate-limiting-bulkhead-concurrency-control-and-request-hedging)
    - [Added](#added)
    - [Fixed](#fixed)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Changed](#changed)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Changed](#changed)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Added](#added)
    - [Changed](#changed)
    - [Added](#added)
  - [🚀 MAJOR PROTOBUF IMPLEMENTATION MILESTONE (August 2025)](#-major-protobuf-implementation-milestone-august-2025)
    - [Changed](#changed)
    - [BREAKING: Protobuf Strategy Migration](#breaking-protobuf-strategy-migration)
    - [Added](#added)
    - [Changed](#changed)
    - [Current Implementation Status (June 2025)](#current-implementation-status-june-2025)
      - [Completed Modules](#completed-modules)
      - [In Progress Modules](#in-progress-modules)
      - [Pending Implementation](#pending-implementation)
    - [Critical Discovery (June 2025)](#critical-discovery-june-2025)
    - [Developer Workflow (June 2025)](#developer-workflow-june-2025)
- [Starting work on issue #68](#starting-work-on-issue-68)
- [Completing work](#completing-work)
  - [Fixed](#fixed)
  - [Technical Documentation](#technical-documentation)
    - [Protobuf Architecture](#protobuf-architecture)
    - [Module Architecture Details](#module-architecture-details)
      - [Health Module (100% Complete)](#health-module-100-complete)
      - [Authentication Module (45% Complete)](#authentication-module-45-complete)
      - [Database Module (30% Complete)](#database-module-30-complete)
      - [Cache Module (20% Complete)](#cache-module-20-complete)
      - [Configuration Module (20% Complete)](#configuration-module-20-complete)
      - [Logging Module (50% Complete)](#logging-module-50-complete)
      - [Metrics Module (70% Complete)](#metrics-module-70-complete)
      - [Queue Module (10% Complete)](#queue-module-10-complete)
      - [Web Module (10% Complete)](#web-module-10-complete)
  - [Implementation Strategy](#implementation-strategy)
    - [Phase 1: Foundation (Weeks 1-4)](#phase-1-foundation-weeks-1-4)
    - [Phase 2: Core Services (Weeks 5-12)](#phase-2-core-services-weeks-5-12)
    - [Phase 3: Advanced Services (Weeks 13-20)](#phase-3-advanced-services-weeks-13-20)
    - [Phase 4: Production Readiness (Weeks 21-24)](#phase-4-production-readiness-weeks-21-24)
  - [Breaking Changes](#breaking-changes)
  - [Migration Guides](#migration-guides)
  - [[0.1.0] - 2024-12-15](#-0-1-0-2024-12-15)
    - [Added](#added)
    - [Technical Foundation](#technical-foundation)
  - [Development Notes](#development-notes)
    - [Code Quality Standards](#code-quality-standards)
    - [Observability Integration](#observability-integration)
    - [Production Considerations](#production-considerations)
  - [Changelog](#changelog)

### Added

- Implemented advanced gRPC client resilience with token bucket rate limiting, bulkhead concurrency control, and request hedging [Added](#added-1)
  - [Added](#added-2)
  - [Added](#added-3)
  - [Added\\n\\n- Expand performance testing framework with runner, benchmarks, load, stress, and regression modules](#addednn--expand-performance-testing-framework-with-runner-benchmarks-load-stress-and-regression-modules)
  - [Added](#added-4)
  - [Added](#added-5)
  - [Added](#added-6)
  - [Added](#added-7)
  - [Added\\n\\n- Implement comprehensive database migration system with versioning, rollback, and multi-database support](#addednn--implement-comprehensive-database-migration-system-with-versioning-rollback-and-multi-database-support)
  - [Added](#added-8)
  - [Added](#added-9)
  - [Added\\n- Implemented advanced gRPC client resilience with token bucket rate limiting, bulkhead concurrency control, and request hedging](#addedn--implemented-advanced-grpc-client-resilience-with-token-bucket-rate-limiting-bulkhead-concurrency-control-and-request-hedging)
  - [Added](#added-10)
  - [Fixed](#fixed)
  - [Added](#added-11)
  - [Added](#added-12)
  - [Added\\n- Scaffold dependency optimization, security scanning, version policy, and metrics tools for Task 18](#addedn--scaffold-dependency-optimization-security-scanning-version-policy-and-metrics-tools-for-task-18)
  - [Added\\n\\n- Expanded auth module with JWT provider, token refresh/validation, ABAC policy engine, gRPC services, middleware, and examples](#addednn--expanded-auth-module-with-jwt-provider-token-refreshvalidation-abac-policy-engine-grpc-services-middleware-and-examples)
  - [Added](#added-13)
  - [Added\\n- Introduced basic HTTP server, logging middleware, and memory session store for web module](#addedn--introduced-basic-http-server-logging-middleware-and-memory-session-store-for-web-module)
  - [Added](#added-14)
  - [Added](#added-15)
  - [Added](#added-16)
  - [Added](#added-17)
  - [Added](#added-18)
  - [Added](#added-19)
  - [Added](#added-20)
  - [Added](#added-21)
  - [Added](#added-22)
  - [Added](#added-23)
  - [Added](#added-24)
  - [Added](#added-25)
  - [Added](#added-26)
  - [Added](#added-27)
  - [Added](#added-28)
  - [Added](#added-29)
  - [Added](#added-30)
  - [Added](#added-31)
  - [Added](#added-32)
  - [Added](#added-33)
  - [Added](#added-34)
  - [Added](#added-35)
  - [Added](#added-36)
  - [Added](#added-37)
  - [Added](#added-38)
  - [Added](#added-39)
  - [Added](#added-40)
  - [Changed\\n\\n- Expanded in-memory metrics provider to handle histograms, summaries, and timers](#changednn--expanded-in-memory-metrics-provider-to-handle-histograms-summaries-and-timers)
  - [Added](#added-41)
  - [Added](#added-42)
  - [Added\\n\\n- Implemented comprehensive integration testing framework](#addednn--implemented-comprehensive-integration-testing-framework)
  - [Added](#added-43)
  - [Added\\n\\n- Added integration testing framework structure with placeholders](#addednn--added-integration-testing-framework-structure-with-placeholders)
  - [Added](#added-44)
  - [Added](#added-45)
  - [Added](#added-46)
  - [Added](#added-47)
  - [Added\\n\\n- Expanded Auth module documentation with detailed guides](#addednn--expanded-auth-module-documentation-with-detailed-guides)
  - [Changed](#changed)
  - [Added](#added-48)
  - [Added\\n- Added config module service skeleton](#addedn--added-config-module-service-skeleton)
  - [Added](#added-49)
  - [Added\\n- Introduced integration testing framework for module and cross-module validation](#addedn--introduced-integration-testing-framework-for-module-and-cross-module-validation)
  - [Added](#added-50)
  - [Added](#added-51)
  - [Added](#added-52)
  - [Added\\n\\n- Enhanced integration test environment with mock services and utilities](#addednn--enhanced-integration-test-environment-with-mock-services-and-utilities)
  - [Added\\n\\n- Complete notification module with providers, templates, delivery tracking, and gRPC services](#addednn--complete-notification-module-with-providers-templates-delivery-tracking-and-grpc-services)
  - [Added](#added-53)
  - [Added\\n- Expanded web module with server factory, middleware, session manager, handlers, routing, gRPC skeleton, and examples](#addedn--expanded-web-module-with-server-factory-middleware-session-manager-handlers-routing-grpc-skeleton-and-examples)
  - [Added](#added-54)
  - [Added\\n- Implemented organization service layer with tenant, hierarchy, and team management](#addedn--implemented-organization-service-layer-with-tenant-hierarchy-and-team-management)
  - [Added](#added-55)
  - [Changed](#changed-1)
  - [Added](#added-56)
  - [🚀 MAJOR PROTOBUF IMPLEMENTATION MILESTONE (August 2025)](#-major-protobuf-implementation-milestone-august-2025)
    - [Changed](#changed-2)
    - [BREAKING: Protobuf Strategy Migration](#breaking-protobuf-strategy-migration)
    - [Added](#added-57)
    - [Changed](#changed-3)
    - [Current Implementation Status (June 2025)](#current-implementation-status-june-2025)
      - [Completed Modules](#completed-modules)
      - [In Progress Modules](#in-progress-modules)
      - [Pending Implementation](#pending-implementation)
    - [Critical Discovery (June 2025)](#critical-discovery-june-2025)
    - [Developer Workflow (June 2025)](#developer-workflow-june-2025)
    - [Fixed](#fixed-1)
    - [Technical Documentation](#technical-documentation)
      - [Protobuf Architecture](#protobuf-architecture)
      - [Module Architecture Details](#module-architecture-details)
        - [Health Module (100% Complete)](#health-module-100-complete)
        - [Authentication Module (45% Complete)](#authentication-module-45-complete)
        - [Database Module (30% Complete)](#database-module-30-complete)
        - [Cache Module (20% Complete)](#cache-module-20-complete)
        - [Configuration Module (20% Complete)](#configuration-module-20-complete)
        - [Logging Module (50% Complete)](#logging-module-50-complete)
        - [Metrics Module (70% Complete)](#metrics-module-70-complete)
        - [Queue Module (10% Complete)](#queue-module-10-complete)
        - [Web Module (10% Complete)](#web-module-10-complete)
    - [Implementation Strategy](#implementation-strategy)
      - [Phase 1: Foundation (Weeks 1-4)](#phase-1-foundation-weeks-1-4)
      - [Phase 2: Core Services (Weeks 5-12)](#phase-2-core-services-weeks-5-12)
      - [Phase 3: Advanced Services (Weeks 13-20)](#phase-3-advanced-services-weeks-13-20)
      - [Phase 4: Production Readiness (Weeks 21-24)](#phase-4-production-readiness-weeks-21-24)
    - [Breaking Changes](#breaking-changes)
    - [Migration Guides](#migration-guides)
  - [\[0.1.0\] - 2024-12-15](#010---2024-12-15)
    - [Added](#added-58)
    - [Technical Foundation](#technical-foundation)
  - [Development Notes](#development-notes)
    - [Code Quality Standards](#code-quality-standards)
    - [Observability Integration](#observability-integration)
    - [Production Considerations](#production-considerations)
  - [Changelog](#changelog)

## [Unreleased]

### Added

- Added examples for config and queue modules (Task 11)
- Added in-memory metrics provider
- Add comprehensive example directory skeleton
- Skeleton Go examples for modules, integration, and production
- Add skeleton database migration framework

### Added

- Standardized logging across modules with
  providers, middleware, aggregation,
  monitoring, and tracing

- Completed remaining auth module protobuf definitions
- Added skeleton for integration test environment
  a

### Added

- Expand monitoring and observability with collectors, alerts, exporters, and dashboards

### Added

- Add initial error handling framework
- Added docsystem scaffolding
- Add skeletons for multi-language client SDKs

Added comprehensive containerization and deployment templates with monitoring and automation

### Added

- Expand performance testing framework with runner, benchmarks, load, stress, and regression modules

### Added

- Add performance testing framework skeleton

### Added

- Added automated API documentation generation script

Implemented organization module service layer with gRPC services

### Added

- Introduced CI/CD pipeline skeleton and quality gate workflow

- auth: add OAuth2 and LDAP providers with token blacklist

### Added

- Added performance testing framework

### Added

- Implement comprehensive database migration system with versioning, rollback, and multi-database support

### Added

- Completed cache module implementation and verification

### Added

- Implemented comprehensive monitoring and observability with collectors,
  exporters, alerts, and dashboards

### Added\n- Implemented advanced gRPC client resilience with token bucket rate limiting, bulkhead concurrency control, and request hedging

feat: unify gRPC server and service registration across modules

### Added

- Add Dockerfile and Kubernetes deployment templates

### Fixed

- Fixed create-issue-update script requiring GH_TOKEN or git remote

### Added

- Add Code of Conduct for community guidelines

### Added

- Implemented notification gRPC service layer with admin operations

### Added

- Scaffold dependency optimization, security scanning, version policy, and metrics tools for Task 18

Enhanced dependency audit script with license checks and conflict detection

### Added

- Expanded auth module with JWT provider, token refresh/validation, ABAC policy engine, gRPC services, middleware, and examples

### Added

- Added SDK generation scaffolding

### Added

- Introduced basic HTTP server, logging middleware, and memory session store for web module

### Added

- Enhanced environment and file configuration sources with file watching

### Added

- Added initial auth service skeleton with local provider and JWT handling

### Added

- Initial queue service layer with memory and redis providers

### Added

- Added initial module documentation skeleton

### Added

- Added memcached cache provider and extended cache service operations

### Added

- Add standardized LogEntry struct for structured logging

### Added

- Add logging wrappers for config, queue, and auth modules for standardized
  logging

### Added

- Add advanced gRPC client utilities with retries and circuit breaker

### Added

- Added production readiness checklist for gcommon modules

Pin otlptranslator dependency and update collectors to new OTel APIs

### Added

- Add initial performance testing framework skeleton

feat(queue): implement queue service layer with memory and redis providers,
scheduler, and monitoring

### Added

- Add comprehensive deployment stack with Docker, Kubernetes, Helm, automation,
  and monitoring

### Added

- Add basic getting started example

### Added

- Document completion of Task 05 web module implementation

### Added

- Scaffold documentation skeleton for module documentation system

### Added

- Added comprehensive logging module with providers, middleware, aggregation,
  and monitoring

### Added

- Add configuration management system enhancements with file source auto
  detection and TOML support

### Added

- Introduce initial microservice template scaffolding

### Added

- Document completion of error handling standardization

### Added

- Implemented comprehensive error handling framework across modules

### Added

- Track automated API documentation generation pipeline (see issue: API Docs:
  Automated generation)

### Added

- Add JWT auth and basic cache examples

### Added

- Added Python and TypeScript SDK implementations and Rust skeleton.

Add organization service layer with in-memory tenant management

Add comprehensive configuration management system skeleton with loaders,
watchers, sources and examples

### Added

- Add buf plugins for generating multi-language SDKs

### Added

- Implemented database migration system with multi-database support and rollback

### Added

- Add notification service layer skeleton

### Added

- Implemented security audit framework with policies, monitoring, and
  cryptographic tools across modules.

### Added

- Add end-to-end integration test scenarios and workflows

### Changed

- Expanded in-memory metrics provider to handle histograms, summaries, and timers

### Added

- Added monitoring infrastructure scaffolding

### Added

- Introduce security module scaffolding

### Added

- Implemented comprehensive integration testing framework

### Added

- Add deployment templates and monitoring configuration

### Added

- Added integration testing framework structure with placeholders

### Added

- Add API documentation generation scaffolding

### Added

- Added gRPC client resilience interceptor combining retries and circuit
  breaking (Refs #882)

- Added gRPC MigrationService server and client

### Added

- Added microservice templates and generator

### Added

- Enhanced CI/CD pipeline with multi-stage testing, quality gates, release
  automation, environment management, and reporting

Added cache service layer with in-memory provider and gRPC service
implementation

### Added

- Expanded Auth module documentation with detailed guides

Added redis and distributed cache providers, eviction policies, serialization,
metrics, and examples

### Changed

- Marked plugin architecture task as complete in tasks documentation.

### Added

- Add unified gRPC service registration scaffold

### Added

- Added config module service skeleton

### Added

- Refine gRPC server registration and lifecycle management

### Added

- Introduced integration testing framework for module and cross-module validation

Added skeleton metrics exporters

### Added

- Expanded web module with Redis-backed sessions, parametric router, compression
  middleware, and admin gRPC service

### Added

- Add configuration manager skeleton

### Added

- Implemented comprehensive security module

### Added

- Enhanced integration test environment with mock services and utilities

### Added

- Complete notification module with providers, templates, delivery tracking, and gRPC services

### Added

- Enhanced CI/CD pipeline with multi-stage testing and quality gates

### Added

- Expanded web module with server factory, middleware, session manager, handlers, routing, gRPC skeleton, and examples

### Added

- Add security scanning workflow for Go and Node dependencies

### Added

- Implemented organization service layer with tenant, hierarchy, and team management

### Added

- Added integration test environment scaffolding.

### Changed

- Marked plugin architecture task as complete in tasks documentation.

### Added

- Added extensible plugin architecture with security, communication bus, SDK,
  and examples
- Add dependency audit script and management policy
- Add Go vulnerability scanning workflow
- Introduce plugin framework skeleton
- Add initial config provider factory with file and env providers
- Expanded module documentation skeletons for all modules

## 🚀 MAJOR PROTOBUF IMPLEMENTATION MILESTONE (August 2025)

**🚀 MASSIVE PROTOBUF EXPANSION**: Completed comprehensive 1-1-1 pattern
implementation across all modules

- **1,279+ Protobuf Files**: Expanded from ~754 to 1,279+ individual proto files
  following 1-1-1 pattern
- **Complete Config Module**: 155 proto files (split from 7 large files into
  individual enum/message files)
- **Complete Queue Module**: 216 proto files (most complex module with
  comprehensive message definitions)
- **Complete Metrics Module**: 172 proto files (full metrics collection and
  provider management)
- **Complete Auth Module**: 172 proto files (comprehensive authentication and
  authorization)
- **Complete Web Module**: 224 proto files (full web server and middleware
  management)
- **Complete Cache Module**: 72 proto files (full caching layer implementation)
- **Expanded Organization Module**: 80 proto files (team and tenant management)
- **Enhanced Notification Module**: 22 proto files (notification delivery
  system)

**🔧 1-1-1 PATTERN AUTOMATION**:

- Created `split_proto.py` for automated proto file splitting
- Implemented `analyze_proto_files.sh` for validation and analysis
- Documented complete splitting process in `PROTO_SPLITTING_GUIDE.md`
- Successfully split 16 large monolithic files into 180+ individual files

**📊 MODULE COMPLETION STATUS**:

- **Config Module**: 100% protobuf structure complete (155/155 files)
- **Queue Module**: 100% protobuf structure complete (216/216 files)
- **Metrics Module**: 100% protobuf structure complete (172/172 files)
- **Auth Module**: 100% protobuf structure complete (172/172 files)
- **Web Module**: 100% protobuf structure complete (224/224 files)
- **Cache Module**: 100% protobuf structure complete (72/72 files)
- **Health Module**: 100% complete and production-ready (35/35 files)
- **Common Module**: 100% complete foundation types (40/40 files)
- **Database Module**: 100% complete and production-ready (52/52 files)
- **Log Module**: 100% complete minimal implementation (14/14 files)

**Previous Achievements**:

- Implemented all Metrics request and response protobufs
- Added DatabaseStatus message and DatabaseStatusCode enum for database module
- Implemented web module message definitions
- Added MediaFile and related types for subtitle-manager support
- Implemented remaining organization protobuf messages
- Implemented metrics request and response protobufs
- Verified completion of all cache protobufs
- Started migrating log protobufs to 1-1-1
- Implemented initial queue configuration messages and enums
- Implemented new auth protobufs: refresh token, security policy, audit event
- Implemented session management protobufs for web module
- Implemented web cache configuration message and admin service
- Verified database module protobufs complete
- Implemented MarkAsRead and Delete notification protobufs
- Implemented Web HealthCheckConfig protobuf
- Implemented additional queue protobufs for listing and pull operations
- Implemented core permission and auth context protobufs
- Added MySQLConfig and MySQLStatus protobuf messages
- Added CockroachDB config protobuf
- Added PebbleConfig protobuf for Pebble driver
- Implemented initial web configuration messages and middleware update
  request/response

### Changed

- Verified common module protobufs fully implemented

### BREAKING: Protobuf Strategy Migration

**🚨 CRITICAL ARCHITECTURAL CHANGE**: Based on Go best practices research, we
are migrating away from `import public` aggregator files to direct imports of
specific proto files.

**Why This Change Is Necessary**:

- `import public` is a C++-centric feature that creates complexity in Go
- Go protobuf compiler must generate type aliases (e.g., `type Foo = foopb.Foo`)
  for backward compatibility
- This feature is obscure and not well-supported across all protobuf backends
- Direct imports make dependencies explicit and easier to understand
- Follows Go's philosophy of explicit over implicit

**Migration Plan**:

1. **Phase 1**: Deprecate aggregator files (auth.proto, cache.proto, etc.) as
   import-only
2. **Phase 2**: Update all consuming code to import specific proto files
   directly
3. **Phase 3**: Remove aggregator files entirely in v0.3.0
4. **Phase 4**: Update buf.yaml to restore IMPORT_NO_PUBLIC lint rule

**Example Migration**:

```protobuf
// OLD (deprecated):
import "pkg/auth/proto/auth.proto";  // Imports everything via public imports

// NEW (recommended):
import "pkg/auth/proto/messages/user.proto";
import "pkg/auth/proto/requests/login_request.proto";
import "pkg/auth/proto/responses/login_response.proto";
```

**Timeline**:

- v0.2.0: Deprecation warnings
- v0.3.0: Remove aggregator files (BREAKING)

### Added

- Database drivers expose GRPCService() registration - closes #132
- Implemented initial auth provider and password reset protobufs
- Implemented Web module protobufs
- Implemented core web protobuf definitions
- Implemented queue acknowledgment messages and types
- Implemented additional metrics message definitions
- Implemented Config module request protobufs
- Completed Cache module protobufs and updated aggregator
- Implemented initial metrics protobufs
- Added 10 log protobuf files and migrated log.proto to aggregator

- Implemented initial auth configuration and API key messages
- Implemented initial Queue protobufs (QueueMessage, DeliveryOptions,
  SendMessageRequest, SendMessageResponse, MessageState)
- Implemented initial metrics protobuf definitions (alerts, stats)
- Organized GitHub project board with standard columns
- Added improved GitHub project setup script with automatic authentication and
  issue linking
- Add shared pagination and sort proto types
- Removed custom add-to-project workflow in favor of built-in GitHub automation
- Added protobuf validation workflow
- Marked Health and Organization protobuf modules complete
- Implemented Web module enumerations
- **Protobuf Foundation**: Complete mapping for all 9 modules with 29 services
  and 754 protobuf files
- **Common Types Module**: 39 shared message types implemented for consistency
  across modules
- **Database Module**: Complete 1-1-1 migration (51/51 types) serving as gold
  standard
- **Health Module**: Complete 1-1-1 migration (36/36 types) with full protobuf
  implementation
- **Auth Module**: Partial implementation (16/48 types) with core authentication
  services functional
- **Documentation**: Comprehensive technical design documents and implementation
  guides
- **Automated Issue Management**: GitHub Actions workflow for programmatic issue
  updates via JSON files
- **gRPC Metrics Middleware**: Unary and streaming interceptors for metrics
  collection
- **Database gRPC Services**: SQLite and CockroachDB drivers expose
  `GRPCService()`

### Changed

- **Issue Management Process**: Now supports automated issue creation, updates,
  and closure via `issue_updates.json`
- **Development Workflow**: Enhanced with automated issue tracking requiring
  status updates for all work

### Current Implementation Status (June 2025)

#### Completed Modules

- **✅ Database Module**: 100% complete - All 51 types migrated to 1-1-1
  structure
- **✅ Common Module**: 100% complete - 39 shared types implemented
- **✅ Health Module**: 100% complete - All 36 types migrated to 1-1-1 structure
- **✅ Log Module**: 100% complete - Minimal logging implementation

#### In Progress Modules

- **🔄 Auth Module**: 33% complete (16/48 types implemented)
- **🔄 Cache Module**: 15% complete (7/46 types implemented)
- **🔄 Config Module**: 9% complete (2/23 types implemented)
- **🔄 Notification Module**: 10% complete (initial message types defined)

#### Pending Implementation

- **❌ Metrics Module**: 1% complete - 94/95 types require implementation
- **❌ Logging Module**: 0% complete - All 50 types require implementation
- **❌ Queue Module**: 1% complete - 142/143 types require implementation
- **❌ Web Module**: 1% complete - 122/123 types require implementation

### Critical Discovery (June 2025)

**⚠️ Major Implementation Gap Identified**: Analysis revealed **626 empty
protobuf files** (83% of 754 total files) requiring immediate implementation.
This represents a significantly larger scope than initially estimated.

**Immediate Priorities**:

1. Complete protobuf message implementations for all modules
2. Enable gRPC service functionality across the stack
3. Standardize error handling with common types
4. Add request metadata to all service methods

### Developer Workflow (June 2025)

**🤖 Automated Issue Management**: All work now requires proper issue status
tracking using the automated GitHub Actions workflow.

**Required Process for All Development Work**:

1. **Start Task**: Assign issue to yourself, mark "in-progress"
2. **During Work**: Reference issue numbers in commits, update progress
3. **Complete Task**: Close issue with completion summary, mark "completed"

**Issue Updates via JSON**: Create `issue_updates.json` with actions (create,
update, delete) and push to main branch for automatic processing.

**Example Workflow**:

```bash
# Starting work on issue #68
echo '[{"action": "update", "number": 68, "assignees": ["username"], "labels": ["in-progress"]}]' > issue_updates.json
git add . && git commit -m "Start work on issue #68: Metrics Messages" && git push

# Completing work
echo '[{"action": "update", "number": 68, "state": "closed", "labels": ["completed"]}]' > issue_updates.json
git add . && git commit -m "Complete issue #68: Implemented all metrics message types" && git push
```

### Fixed

- **Protobuf Compilation Issues**: Resolved all import path and syntax errors
  across auth and common packages
  - Fixed 8+ protobuf files with import path errors (`gcommon/v1/` → `pkg/`
    relative paths)
  - Corrected invalid `[lazy = true]` field options on primitive types (strings,
    repeated strings)
  - Removed unused imports (`google/protobuf/duration.proto`,
    `google/protobuf/empty.proto`)
  - Standardized import paths across all auth and common package protobuf files
- **Service Definition Cleanup**: Systematically commented out incomplete
  service methods while preserving working functionality
  - AuthService: 2 working methods (`Authenticate`, `ValidateToken`)
  - SessionService: 1 working method (`CreateSession`)
  - AuthorizationService: Temporarily disabled (awaiting missing message types)
- **Protobuf Import Consistency**: All proto files now use consistent relative
  import paths for cross-module dependencies

### Technical Documentation

#### Protobuf Architecture

- **Common Types**: 25+ shared message types for consistency across all modules
- **Service Definitions**: 21 total services distributed across 9 modules
- **Message Catalog**: 400+ message definitions covering all functionality
- **Implementation Phases**: 4-phase rollout strategy for systematic
  implementation

#### Module Architecture Details

##### Health Module (100% Complete)

- **Services**: HealthService with 10 methods
- **Messages**: 25+ request/response pairs
- **Features**: Kubernetes probes, Prometheus metrics, remediation actions
- **Integrations**: Full observability stack integration

##### Authentication Module (45% Complete)

- **Services**: AuthService, AuthorizationService, SessionService (23 methods
  total)
- **Messages**: 60+ message definitions (most complex module)
- **Features**: Multi-factor auth, RBAC, session management, token lifecycle
- **Security**: Built-in rate limiting, audit logging, secure defaults
- **Status**: Protobuf definitions complete, compilation issues resolved, core
  service methods functional (Authenticate, ValidateToken, CreateSession)

##### Database Module (30% Complete)

- **Services**: DatabaseService, TransactionService, SchemaService,
  MigrationService (22 methods)
- **Messages**: 50+ message definitions
- **Backends**: SQLite, PostgreSQL, CockroachDB, Pebble support
- **Features**: ACID transactions, schema migrations, connection pooling

##### Cache Module (20% Complete)

- **Services**: CacheService, CacheManagementService (18 methods)
- **Messages**: 35+ message definitions
- **Backends**: Redis, Memcached, in-memory support planned
- **Features**: TTL management, batch operations, statistics

##### Configuration Module (20% Complete)

- **Services**: ConfigService, ConfigSchemaService (13 methods)
- **Messages**: 30+ message definitions
- **Features**: Hot reload, schema validation, environment management
- **Sources**: File, environment, remote configuration support

##### Logging Module (50% Complete)

- **Services**: LogService, LogManagementService (13 methods)
- **Messages**: 30+ message definitions
- **Backends**: Standard library, Zap, Logrus support
- **Features**: Structured logging, log aggregation, filtering

##### Metrics Module (70% Complete)

- **Services**: MetricsService, MetricsManagementService (13 methods)
- **Messages**: 35+ message definitions
- **Backends**: Prometheus, OpenTelemetry support
- **Features**: Custom metrics, aggregation, alerting integration

##### Queue Module (10% Complete)

- **Services**: QueueService, QueueManagementService (18 methods)
- **Messages**: 30+ message definitions
- **Backends**: RabbitMQ, NATS, AWS SQS support planned
- **Features**: Batch processing, dead letter queues, retry logic

##### Web Module (10% Complete)

- **Services**: WebService, MiddlewareService, WebSocketService (19 methods)
- **Messages**: 40+ message definitions
- **Features**: Middleware chain, WebSocket support, security headers
- **Integrations**: Authentication, metrics, logging built-in

### Implementation Strategy

#### Phase 1: Foundation (Weeks 1-4)

1. **Common Types Enhancement**: Add remaining 6 message types to common.proto
2. **Protobuf Standardization**: Update all existing proto files to use common
   types
3. **Health Module Optimization**: Performance improvements and additional
   checks
4. **Metrics Module Completion**: Finish OpenTelemetry integration

#### Phase 2: Core Services (Weeks 5-12)

1. **Database Module**: Complete all 4 services with full backend support
2. **Cache Module**: Implement all backends and management features
3. **Configuration Module**: Hot reload and schema validation
4. **Logging Module**: Complete gRPC services and aggregation

#### Phase 3: Advanced Services (Weeks 13-20)

1. **Authentication Module**: Complete RBAC and session management
2. **Queue Module**: Implement all backends and batch processing
3. **Web Module**: Complete middleware system and WebSocket support

#### Phase 4: Production Readiness (Weeks 21-24)

1. **Performance Optimization**: Benchmarking and optimization across all
   modules
2. **Integration Testing**: End-to-end testing with real-world scenarios
3. **Documentation**: Complete API documentation and examples
4. **Security Audit**: Security review and penetration testing

### Breaking Changes

- **v0.2.0**: Protobuf message structure changes (planned)
- **v0.3.0**: Authentication API changes (planned)

### Migration Guides

- Will be added as breaking changes are introduced

## [0.1.0] - 2024-12-15

### Added

- Initial project structure
- Health module with basic functionality
- Metrics module foundation
- Logging module interfaces
- Basic examples and documentation

### Technical Foundation

- go 1.23+ requirement
- Protocol Buffers for service definitions
- gRPC for network services
- OpenTelemetry for observability
- MIT License

---

## Development Notes

### Code Quality Standards

- 90%+ test coverage for all modules
- Comprehensive documentation for all public APIs
- Consistent error handling patterns
- Performance benchmarks for critical paths

### Observability Integration

- All modules integrate with metrics collection
- Structured logging with correlation IDs
- Distributed tracing support
- Health checks for all services

### Production Considerations

- Graceful shutdown handling
- Configuration validation
- Rate limiting and circuit breakers
- Security best practices
- Kubernetes deployment examples

---

_This changelog consolidates technical documentation that would otherwise be
scattered across multiple files, following the GCommon documentation
organization policy._

## Changelog

- **Feature**: Added DebugInfo message for enhanced debugging metadata
- **Feature**: Added TransactionService and MigrationService with new
  request/response messages
