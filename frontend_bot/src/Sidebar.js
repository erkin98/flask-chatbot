import React from "react";
import "./Sidebar.css";
import SidebarChat from "./SidebarChat";
import { useStateValue } from "./StateProvider";
import { IconButton } from "@material-ui/core";
import RefreshIcon from '@material-ui/icons/Refresh';

function Sidebar({refreshHandler}) {
  const [state] = useStateValue();

  return (
    <div className="sidebar">
      <div className="sidebar__header">
        <div className="header__userInfo">
          <h3>WhatsApp Bot</h3>
        </div>
        <div className="sidebar__headerRight">
          <IconButton onClick={refreshHandler}>
            <RefreshIcon />
          </IconButton>
        </div>
      </div>
      <div className="sidebar__chats">
        {state.customers.map((c,idx)=> <SidebarChat key={`customer-${idx}`} name={c} id={idx}/>)}
      </div>
    </div>
  );
}

export default Sidebar;
