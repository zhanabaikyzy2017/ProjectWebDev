export interface IAuthor{
    id:number;
    name:string;
    surname:string;
    date_of_birth:string;
    date_of_death:string;
}

export interface IPublisher{
    name:string;
}

export interface IUser{
    id:number;
    username:string;
    password:string;
    email:string;
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
    id:number;
    name:string;
}

export interface IBook{
    id:number;
    title:string;
    category:any;
    description:string;
    year:number;
    author: IAuthor
    page_amount:number;
    added_by:IUserProfile;
    image:any;
}
export interface IReview{
    user:IUser;
    book:IBook;
    text:string;
    creation_date:any;
}
export interface IAuthResponse{
    token: string;
    is_staff:boolean;
}