export interface IAuthor{
    name:string;
    surname:string;
    date_of_birth:any;
}

export interface IPublisher{
    name:string;
}

export interface IUser{
    userID:number;
    username:string;
    // password:string;
    // email:string;
}
export interface IUserProfile{
    id:number;
    user: IUser;
    mobile:string;
    website:string;
    join_date:any;
    book:IBook[];
}

export interface ICategory{
    name:string;
}

export interface IBook{
    title:string;
    category:any;
    description:string;
    year:number;
    author: IAuthor
    publisher:IPublisher
    page_amount:number;
    added_by:IUserProfile;
    image:any;
}

export interface IQuotation{
    user:IUser;
    book:IBook;
    quotation:string;
    creation_date:any;
}
export interface IAuthResponse{
    token: string;
}