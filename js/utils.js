import querystring from "query-string";


export const stringifyParams = (params) => {
  let pageParams = null;
  let restParams = null;

  // if (page && Object.entries(page).length > 0) {
  //   pageParams = Object.keys(page).reduce((string, paramName) => {
  //     if (string.length > 0) {
  //       string += "&";
  //     }

  //     string += `page[${paramName}]=${page[paramName]}`;

  //     return string;
  //   }, "");
  // }

  if (params && Object.entries(params).length > 0) {
    return "?" + querystring.stringify(params)
  }

  return "";
};
