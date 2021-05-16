export interface APIKey {
    type: "Third party";
    company: string;
}

export const isAPIKey = (object: any): object is APIKey =>{
    try {
        if (object.company && object.type === "Third party"){
            return true
        } else {
            return false
        }
    } catch (error) {
        return false
    }
        
}