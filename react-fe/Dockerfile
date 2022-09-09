#get the base node image
FROM node:alpine as builder

ENV NODE_ENV production
#Set the working dir for container
WORKDIR /frontend

#copy the json file first to working dir folder in containter

COPY ./package.json /frontend


#Install npm dependancies
RUN npm install --production

# Copy other project files
COPY . .

# build the folder
RUN npm run build
# CMD ["npm","run","start"]

# Stage 2

FROM nginx:1.23.1-alpine as production
ENV NODE_ENV production

#COPY build assets from builder

COPY --from=builder /frontend/build /usr/share/nginx/html

#Add nginx.conf

COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

# EXPOSE PORT
EXPOSE 80 443

# START nginx

CMD ["nginx","-g","daemon off;"]