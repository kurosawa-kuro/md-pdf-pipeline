# grep: env_secret

evidence_id: ev.grep.env_secret
description: env / secret / credential

- doppler.yaml:L9: # 非機密の設定値は env/config.yaml、ローカルだけの秘密情報は env/secret.yaml に置く。
- doppler.yaml:L10: # env/secret.yaml は .gitignore で除外し、コミットしない。
- doppler.yaml:L16: # AUTH_SECRET_KEY
- doppler.yaml:L22: # AI_OPENAI_API_KEY
- doppler.yaml:L33: # AWS_SECRET_ACCESS_KEY
- env/config.yaml:L4: # ローカル秘密情報は env/secret.yaml、共有・本番クレデンシャルは Doppler で管理 (doppler.yaml)
