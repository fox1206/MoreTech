// Create section Header for application
import {AppBar, List, ListItem, ListItemText, ListItemButton, Container, Toolbar, Typography} from '@mui/material';
import React from 'react';
import Link from 'next/link';
import Box from '@mui/material/Box';
import MenuIcon from '@mui/icons-material/Menu';
import TextField from '@mui/material/TextField';
import NotificationsNoneIcon from '@mui/icons-material/NotificationsNone';
import NightlightOutlinedIcon from '@mui/icons-material/NightlightOutlined';
import GridViewOutlinedIcon from '@mui/icons-material/GridViewOutlined';
import Avatar from '@mui/material/Avatar';

// массив с хранением названия и ссылки на страницу
const menuItems = [
    {nameLink: "Главная", path: '/'},
    {nameLink: "Маркетплейс", path: '/shop'},
    {nameLink: "Банк идей", path: '/idea'},
    {nameLink: "События", path: '/event'}, ];

const Header = ({children}) => {
   return(
    <>
    <Box>
      
        <AppBar position='static'
        sx={{display: 'flex', justifyContent: 'space-between', backgroundColor: '#1E2235'}}>
          <Container className='header' maxWidth='xl' sx={{display: 'flex', justifyContent: 'space-between'}}>
            <Box sx={{
              display: 'flex',
              alignItems: 'center',
              columnGap: '15px'
            }}>
              <MenuIcon />
              <img src='../assets/image/svg/logo.svg' alt='logo'/>
            </Box>
            
            <Toolbar className='header__panel' disableGutters>
              <List className='header__list' sx={{display: 'flex'}}>
                {menuItems.map((list) => {
                  return <Link href={list.path}><ListItem className='header__list_item'
                            sx={{whiteSpace: 'nowrap', fontSize: '18px', fontWeight: 600, color: '#ABADC6'}}
                            button
                            key={list.nameLink}
                            >
                    <ListItemText primary={list.nameLink}/>
                    </ListItem></Link>})}
              </List>
            </Toolbar>

            <Box component="form"
              sx={{
                '& .MuiTextField-root': { m: 2, width: '271px' },
                display: 'flex',
                alignItems: 'center',
                columnGap: '30px'
              }}
              noValidate
              autoComplete="off"
              >
                <TextField id="outlined-search" label="Поиск" type="search" />
                <NotificationsNoneIcon />
                <NightlightOutlinedIcon />
                <GridViewOutlinedIcon />
                <Avatar><Link href="/1">A</Link></Avatar>
              </Box>
          </Container>
        </AppBar>
      
      </Box>
      {children}
    </>    
  );
}

export default Header;