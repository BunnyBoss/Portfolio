import { Suspense, useRef } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import {
  Decal,
  Float,
  OrbitControls,
  Preload,
  useTexture,
} from "@react-three/drei";
import Loader from "../Loader";

const Ball = ({ imgUrl, name }) => {
  // For emoji-based icons, we create a procedural sphere
  const meshRef = useRef();

  useFrame((state) => {
    meshRef.current.rotation.y = state.clock.getElapsedTime() * 0.3;
  });

  return (
    <Float speed={1.75} rotationIntensity={1} floatIntensity={2}>
      <ambientLight intensity={0.25} />
      <directionalLight position={[0, 0, 0.05]} />
      <mesh ref={meshRef} castShadow receiveShadow scale={2.75}>
        <icosahedronGeometry args={[1, 1]} />
        <meshStandardMaterial
          color="#151030"
          polygonOffset
          polygonOffsetFactor={-5}
          flatShading
        />
      </mesh>
    </Float>
  );
};

const BallCanvas = ({ icon, name }) => {
  return (
    <div className="flex flex-col items-center">
      <Canvas
        frameloop="demand"
        dpr={[1, 2]}
        gl={{ preserveDrawingBuffer: true }}
        style={{ width: 112, height: 112 }}
      >
        <Suspense fallback={<Loader />}>
          <OrbitControls enableZoom={false} />
          <Ball imgUrl={icon} name={name} />
        </Suspense>
        <Preload all />
      </Canvas>
      <p className="text-secondary text-[12px] mt-1 text-center">{name}</p>
    </div>
  );
};

export default BallCanvas;
