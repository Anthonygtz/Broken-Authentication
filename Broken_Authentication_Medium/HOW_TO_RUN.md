# BROKEN_AUTHENTICATION_MEDIUM

### Requirements

To run the application, you need to have **Docker** installed on your system.

### Running the Application with Docker

1. Build the Docker image:

    ```
    sudo docker build -t broken_authentication_medium .
    ```

2. Run the Docker container:

    ```
    sudo docker run --name broken_authentication_medium -p 5000:5000 -d broken_authentication_medium
    ```

3. Open your web browser and visit the application at:

    ```
    http://localhost:5000
    ```

### Stopping and Removing the Container

1. To stop the running container:
    ```
    sudo docker stop broken_authentication_medium
    ```

2. To remove the container:
    ```
    sudo docker rm broken_authentication_medium
    ```
