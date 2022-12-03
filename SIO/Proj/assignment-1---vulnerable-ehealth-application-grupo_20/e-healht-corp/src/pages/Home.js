import { Carousel } from 'react-bootstrap';
import React, { useState } from 'react';

export function Home() {
    const [index, setIndex] = useState(0);
  
    const handleSelect = (selectedIndex, e) => {
      setIndex(selectedIndex);
    };
    return (
        <Carousel activeIndex={index} onSelect={handleSelect}>
          <Carousel.Item>
            <img
              className="d-block w-100"
              src={require('./assets/health2.jpeg')} width="100" height="730"
              alt="First slide"
            />
            <Carousel.Caption>
              <h3>eHealth Corp</h3>
              </Carousel.Caption>
          </Carousel.Item>
          <Carousel.Item>
            <img
              className="d-block w-100"
              src={require('./assets/health3.jpeg')} width="100" height="730"
              alt="Second slide"
            />
          </Carousel.Item>
          <Carousel.Item>
            <img
              className="d-block w-100"
              src={require('./assets/bg_image_1.jpg')} width="100" height="730"
              alt="Third slide"
            />
          </Carousel.Item>
        </Carousel>
    );   
}
