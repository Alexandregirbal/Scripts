import { APIKeyToken, UserDataToken } from "interfaces";
import { APIKey } from "Services/ThirdParties/interfaces";
import { UserData } from "Services/Users/interfaces";

export {};

declare global {
    namespace Express {
        interface Request {
            decodedToken?: UserDataToken | APIKeyToken;
        }
    }
}