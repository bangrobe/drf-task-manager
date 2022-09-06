import React, { useContext } from "react";
import { Navigate, Outlet } from "react-router-dom";
import { AuthContext } from "src/context/AuthContextProvider";
import LoadingOverlayResource from "./LoadingOverlayResource";
import Toolbar from "@mui/material/Toolbar";
import { Box } from "@mui/system";

const RequireAuth = () => {
  const { isAuthenticated } = useContext(AuthContext);

  if (isAuthenticated === null) {
    return (
      <LoadingOverlayResource>
        <Box
          sx={{
            flexGrow: 1,
            padding: (theme) => theme.spacing(3),
          }}
        >
          <Toolbar />
          <Box>
            <Outlet />
          </Box>
        </Box>
      </LoadingOverlayResource>
    )
  }
  if (isAuthenticated === true) {
    return <Outlet />;
  }
  return <Navigate to="/auth/signin" />;
};

export default RequireAuth;
