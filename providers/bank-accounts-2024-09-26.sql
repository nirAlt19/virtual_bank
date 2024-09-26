CREATE TABLE "bank_accounts"(
    "id" UUID NOT NULL,
    "owner" TEXT NOT NULL,
    "account_type" BIGINT NOT NULL,
    "balance" FLOAT(53) NOT NULL,
    "created_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "updated_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL
);
CREATE INDEX "bank_accounts_owner_index" ON
    "bank_accounts"("owner");
ALTER TABLE
    "bank_accounts" ADD PRIMARY KEY("id");
ALTER TABLE
    "bank_accounts" ADD CONSTRAINT "bank_accounts_owner_unique" UNIQUE("owner");