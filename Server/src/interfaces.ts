import { APIKey } from "Services/ThirdParties/interfaces";
import { UserData } from "Services/Users/interfaces";

export interface DecodedTokenMetaData {
    iat: number;
    exp: number;
}

export interface UserDataToken extends DecodedTokenMetaData {
    user: UserData
}
export interface APIKeyToken extends DecodedTokenMetaData {
    key: APIKey
}