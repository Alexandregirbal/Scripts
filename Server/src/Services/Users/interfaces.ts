export interface UserData {
    firstname: string;
    lastname: string;
    email: string;
    company: string;
    accessRights: string[];
    admin?: boolean;
}

export interface UserSignupData extends UserData {
    password: string;
}

export interface UserCredentials {
    email?: string;
    password?: string;
}