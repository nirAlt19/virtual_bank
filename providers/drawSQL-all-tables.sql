CREATE TABLE "users"(
    "id" UUID NOT NULL,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "password_hash" TEXT NOT NULL,
    "created_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "updated_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL
);
CREATE INDEX "users_email_index" ON
    "users"("email");
ALTER TABLE
    "users" ADD PRIMARY KEY("id");
ALTER TABLE
    "users" ADD CONSTRAINT "users_email_unique" UNIQUE("email");
CREATE TABLE "bank_accounts"(
    "id" UUID NOT NULL,
    "owner" TEXT NOT NULL,
    "account_type" BIGINT NOT NULL,
    "balance" FLOAT(53) NOT NULL,
    "created_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "updated_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL
);
ALTER TABLE
    "bank_accounts" ADD PRIMARY KEY("id");
CREATE INDEX "bank_accounts_owner_index" ON
    "bank_accounts"("owner");
ALTER TABLE
    "bank_accounts" ADD CONSTRAINT "bank_accounts_owner_foreign" FOREIGN KEY("owner") REFERENCES "users"("email");