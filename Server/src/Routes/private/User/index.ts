export default async (req: any, res: any) => {
    console.log(req.user);
        
    return res.status(200).send(req.user)
}