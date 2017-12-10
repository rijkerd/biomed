import React from "react";
import sidePanel from './sidePanel';
//import { connect } from "react-redux";

class Header extends React.Component {
  
  render() {
    return (
      <div>
        <nav>
          <div className="nav-wrapper">
            <a href="/" className="brand-logo center">
              CLASS-APP
            </a>
            <ul style={{marginLeft:10}} className="hide-on-med-and-down">
              <li><a><i className="material-icons">dehaze</i></a></li>
            </ul>
          </div>
        </nav>
      </div>
    );
  }
}

export default Header;
