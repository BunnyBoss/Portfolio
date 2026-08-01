import { Suspense, useRef, useMemo } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import { OrbitControls, Preload } from "@react-three/drei";
import * as THREE from "three";
import Loader from "../Loader";

const Globe = () => {
  const meshRef = useRef();
  const wireRef = useRef();

  // Create latitude/longitude lines
  useFrame((state) => {
    if (meshRef.current) {
      meshRef.current.rotation.y = state.clock.getElapsedTime() * 0.15;
    }
    if (wireRef.current) {
      wireRef.current.rotation.y = state.clock.getElapsedTime() * 0.15;
    }
  });

  // Create dots on the sphere surface
  const dots = useMemo(() => {
    const positions = [];
    for (let i = 0; i < 200; i++) {
      const phi = Math.acos(-1 + (2 * i) / 200);
      const theta = Math.sqrt(200 * Math.PI) * phi;
      positions.push([
        1.02 * Math.cos(theta) * Math.sin(phi),
        1.02 * Math.sin(theta) * Math.sin(phi),
        1.02 * Math.cos(phi),
      ]);
    }
    return positions;
  }, []);

  return (
    <group>
      {/* Inner sphere */}
      <mesh ref={meshRef}>
        <sphereGeometry args={[1, 32, 32]} />
        <meshStandardMaterial
          color="#0a0a2e"
          transparent
          opacity={0.8}
        />
      </mesh>
      {/* Wireframe overlay */}
      <mesh ref={wireRef}>
        <sphereGeometry args={[1.01, 20, 20]} />
        <meshStandardMaterial
          color="#10b981"
          wireframe
          transparent
          opacity={0.2}
        />
      </mesh>
      {/* Surface dots */}
      {dots.map((pos, i) => (
        <mesh key={i} position={pos}>
          <sphereGeometry args={[0.008, 8, 8]} />
          <meshStandardMaterial
            color={i % 5 === 0 ? "#10b981" : "#d4a574"}
            emissive={i % 5 === 0 ? "#10b981" : "#d4a574"}
            emissiveIntensity={0.8}
          />
        </mesh>
      ))}
      {/* Glowing ring */}
      <mesh rotation={[Math.PI / 2, 0, 0]}>
        <torusGeometry args={[1.3, 0.005, 16, 100]} />
        <meshStandardMaterial
          color="#10b981"
          emissive="#10b981"
          emissiveIntensity={1}
        />
      </mesh>
      <mesh rotation={[Math.PI / 2.5, 0.3, 0]}>
        <torusGeometry args={[1.5, 0.003, 16, 100]} />
        <meshStandardMaterial
          color="#d4a574"
          emissive="#d4a574"
          emissiveIntensity={0.6}
          transparent
          opacity={0.6}
        />
      </mesh>
    </group>
  );
};

const EarthCanvas = () => {
  return (
    <Canvas
      shadows
      frameloop="always"
      dpr={[1, 2]}
      gl={{ preserveDrawingBuffer: true }}
      camera={{ fov: 45, near: 0.1, far: 200, position: [-4, 3, 6] }}
    >
      <Suspense fallback={<Loader />}>
        <OrbitControls
          autoRotate
          autoRotateSpeed={0.8}
          enableZoom={false}
          maxPolarAngle={Math.PI / 2}
          minPolarAngle={Math.PI / 2}
        />
        <ambientLight intensity={0.2} />
        <pointLight position={[5, 5, 5]} intensity={1} color="#10b981" />
        <pointLight position={[-5, -5, 5]} intensity={0.3} color="#d4a574" />
        <Globe />
      </Suspense>
      <Preload all />
    </Canvas>
  );
};

export default EarthCanvas;
