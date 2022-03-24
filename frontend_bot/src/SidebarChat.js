import React from "react";
import "./SidebarChat.css";
import { Avatar, makeStyles } from "@material-ui/core";
import { Link } from "react-router-dom";
import PersonIcon from '@material-ui/icons/Person';
const useStyles = makeStyles((theme) => ({
  large: {
    width: "50px",
    height: "50px",
  },
}));

function SidebarChat({ id, addNewChat, name }) {
  const classes = useStyles();

  return !addNewChat ? (
    <Link to={`/rooms/${id}`}>
      <div className="sidebarChat">
        <Avatar
          src={<PersonIcon/>}
          className={classes.large}
        />
        
        <div className="sidebarChat__info">
          <h3>{name}</h3>
        </div>
      </div>
    </Link>
  ) : (
    <div onClick={()=>{}} className="sidebarChat">
      <h2>Add new Chat</h2>
    </div>
  );
}

export default SidebarChat;
