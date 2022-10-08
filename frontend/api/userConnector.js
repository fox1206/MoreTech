import axios from "axios";

export async function UserConnector({setUser}){
    const user = await axios("")
    return setUser(user.data)
}

export async function activeUsers({set}){
    const active = await axios("")
    return active.data
}

export async function orderUser({user}){
    const order = await axios("" + user.id)
}