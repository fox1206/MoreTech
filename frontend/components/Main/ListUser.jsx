import React from "react";
import {List, ListItem, ListItemAvatar, Box, Typography} from "@mui/material";

const users = [
  {name: "Albert Flores", summa: "$12.202", lastSumma: "+12%", id: 1}, {name: "Theresa Webb", summa: "$10.582", lastSumma: "+9%", id: 2}, {name: "Floyd Miles", summa: "$8.954", lastSumma: "+5%", id: 3}, {name: "Annette Black", summa: "$6.719", lastSumma: "-2%", id: 4}
];

export const ListUser = () => {
  return (
    <List sx={{width: '100%'}}>
        {users.map((user) => {
          return <ListItem sx={{
            display: 'flex',
            justifyContent: 'space-between',
            paddingLeft: 0,
            paddingRight: 0
          }} key={user.id}>
          <Box
            sx={{
              width: 44,
              height: 44,
              backgroundColor: '#424867',
              borderRadius: 50
            }}
          ></Box>
            <Box>
              <Typography sx={{
                fontSize: 12,
                color: '#ABADC6'
              }}>{user.name}</Typography>
              {user.lastSumma.includes("+")? <Typography sx={{
                fontSize: 12,
                color: '#22C55E',
                textAlign: 'center',
              }}>{user.lastSumma}</Typography>
              : <Typography sx={{
                fontSize: 12,
                color: '#EF4444',
                textAlign: 'center',
              }}>{user.lastSumma}</Typography>}
            </Box>

            <Typography sx={{
                fontSize: 16,
                alignSelf: 'center'
              }}>{user.summa}</Typography>
          </ListItem>
        })}
      </List>
  );
}
