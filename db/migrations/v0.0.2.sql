ALTER TABLE users ADD username text;
ALTER TABLE users ADD disabled bool;
ALTER TABLE users ADD full_name text;
ALTER TABLE public.users RENAME COLUMN "name" TO username;
ALTER TABLE users ADD hashed_password text;
ALTER TABLE users ADD COLUMN user_role text;