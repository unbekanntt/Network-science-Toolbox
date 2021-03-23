function dFCstream_3D = Vec2Matrix(dFCstream_2D)

% FUNCTION dFCstream_3D = Matrix2Vec(dFCstream_2D)
% takes '2D' dFCstream as input and convert it to '3D' dFCstream
%
% Reference: Lucas Arbabyazd et al. (2020) MethodsX

if (ndims(dFCstream_2D) == 3)
    disp('You do not need this function since your dFCstream is alread 3D')
    return
end

l = size(dFCstream_2D,1);
t = size(dFCstream_2D,2);
n = (1+sqrt(1+8*l))/2;
CN=nchoosek(1:n,2);
dFCstream_3D=zeros(n,n,t);

for i = 1:l
    dFCstream_3D(CN(i,1),CN(i,2),:)=dFCstream_2D(i,:);
end

dFCstream_3D = dFCstream_3D + permute(dFCstream_3D, [2 1 3]);
