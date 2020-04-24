
CREATE TABLE public.device_types (
                id VARCHAR NOT NULL,
                description VARCHAR NOT NULL,
                CONSTRAINT device_types_pk PRIMARY KEY (id)
);


CREATE TABLE public.users (
                id INTEGER NOT NULL,
                email VARCHAR NOT NULL,
                first_name VARCHAR NOT NULL,
                last_name VARCHAR NOT NULL,
                nick_name VARCHAR NOT NULL,
                CONSTRAINT user_pk PRIMARY KEY (id)
);


CREATE UNIQUE INDEX email_unq
 ON public.users
 ( email );

CREATE TABLE public.homes (
                id VARCHAR NOT NULL,
                name VARCHAR NOT NULL,
                user_id INTEGER NOT NULL,
                CONSTRAINT home_pk PRIMARY KEY (id)
);


CREATE UNIQUE INDEX name_idx
 ON public.homes
 ( name );

CREATE TABLE public.rooms (
                id VARCHAR NOT NULL,
                name VARCHAR NOT NULL,
                home_id VARCHAR NOT NULL,
                CONSTRAINT rooms_pk PRIMARY KEY (id)
);


CREATE TABLE public.devices (
                id VARCHAR NOT NULL,
                state VARCHAR NOT NULL,
                name VARCHAR NOT NULL,
                access_level INTEGER NOT NULL,
                room_id VARCHAR NOT NULL,
                type_id VARCHAR NOT NULL,
                CONSTRAINT devices_pk PRIMARY KEY (id)
);


CREATE TABLE public.accesses (
                home_id VARCHAR NOT NULL,
                user_id INTEGER NOT NULL,
                room_id VARCHAR NOT NULL,
                level INTEGER NOT NULL,
                CONSTRAINT access_pk PRIMARY KEY (home_id, user_id, room_id)
);


ALTER TABLE public.devices ADD CONSTRAINT device_types_devices_fk
FOREIGN KEY (type_id)
REFERENCES public.device_types (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.homes ADD CONSTRAINT users_homes_fk
FOREIGN KEY (user_id)
REFERENCES public.users (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.accesses ADD CONSTRAINT users_accesses_fk
FOREIGN KEY (user_id)
REFERENCES public.users (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.rooms ADD CONSTRAINT homes_rooms_fk
FOREIGN KEY (home_id)
REFERENCES public.homes (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.accesses ADD CONSTRAINT homes_accesses_fk
FOREIGN KEY (home_id)
REFERENCES public.homes (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.accesses ADD CONSTRAINT rooms_accesses_fk
FOREIGN KEY (room_id)
REFERENCES public.rooms (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.devices ADD CONSTRAINT rooms_devices_fk
FOREIGN KEY (room_id)
REFERENCES public.rooms (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;
